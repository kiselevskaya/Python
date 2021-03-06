# -*- coding: utf-8 -*-
# pet_shop_server.py

from http.server import HTTPServer, BaseHTTPRequestHandler
from main import *
import time
import os
from collections import OrderedDict
import json
from threading import Thread, Lock
import base64

PORT = 8000
shop = create_shop()
mu = Lock()


class Server(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.get_index_html("/html/index.html")
        if self.path == "/scr.js":
            self.get_index_html("/html/scr.js")
        if self.path == "/zoo_shop_state":
            self.zoo_shop_state()
        if self.path == "/zoo_shop_logs":
            self.zoo_shop_logs()
        if self.path == "/table_animals.js":
            self.get_index_html("/html/table_animals.js")
        if self.path == "/style.css":
            self.get_index_css("/css/style.css")
        if self.path == "/favicon.ico":
            self.get_icon("/html/favicon.ico")

    def get_icon(self, path):
        f = open((os.getcwd() + path), 'rb')
        self.send_response(200)
        self.send_header('Content-Type', 'image/x-icon')
        self.end_headers()
        # self.wfile.write(base64.b64decode(f.read()))
        self.wfile.write(f.read())
        f.close()

    def get_index_css(self, path):
        f = open(os.getcwd() + path)
        self.send_response(200)
        self.send_header('Content-Type', 'text/css')
        self.end_headers()
        self.wfile.write(f.read().encode())
        f.close()

    def get_index_html(self, path):
        f = open(os.getcwd() + path)
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(f.read().encode())
        f.close()

    def zoo_shop_state(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        res = []
        mu.acquire()
        try:
            localtime = time.asctime(time.localtime(time.time()))
            for i in shop.get_animals():
                keys = ['species', 'gender', 'name', 'age', 'weight', 'lifespan', 'obesity', 'description']
                values = [i.species, i.gender, i.name, round(i.age, 2), round(i.weight, 2), i.lifespan, i.obesity, i.description]
                dictionary = OrderedDict(zip(keys, values))
                res.append(dictionary)
            data = {'title': 'Pet Shop', 'data_time': localtime, 'animals': res}
            self.wfile.write(json.dumps(data, indent=4).encode())
        except IndexError:
            self.wfile.write(json.dumps('Pet Shop is empty', indent=4).encode())
        mu.release()

    def zoo_shop_logs(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        res = []
        mu.acquire()
        try:
            for log in shop.get_logs():
                keys = ['localtime', 'log']
                values = [log[0], log[1]]
                dictionary = OrderedDict(zip(keys, values))
                res.append(dictionary)
            self.wfile.write(json.dumps(res, indent=4).encode())
        except IndexError:
            self.wfile.write(json.dumps('The number of animals has not changed', indent=4).encode())
        mu.release()


def check_shop(httpd):
    mu.acquire()
    animal_len = len(shop.get_animals())
    mu.release()
    while animal_len > 0:
        time.sleep(3)
        mu.acquire()
        animal_len = len(shop.get_animals())
        shop.ticker()
        mu.release()
    httpd.shutdown()


def main():
    handler = Server

    httpd = HTTPServer(("localhost", PORT), handler)
    print("serving at port", PORT)

    thread = Thread(target=check_shop, args=(httpd, ))
    thread.start()
    httpd.serve_forever()
    thread.join()


if __name__ == '__main__':
    main()
