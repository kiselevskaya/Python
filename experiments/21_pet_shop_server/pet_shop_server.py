# -*- coding: utf-8 -*-
# pet_shop_server.py

from http.server import HTTPServer, BaseHTTPRequestHandler
from main import *
import time
import os
from threading import Thread, Lock

PORT = 8000
shop = create_shop()
mu = Lock()


class Server(BaseHTTPRequestHandler):

    def _set_headers(self):
        # Send response status code
        self.send_response(200)
        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        if self.path == "/":
            self.get_index_html()
        if self.path == "/zoo_shop_state":
            self.zoo_shop_state()

    def get_index_html(self):
        f = open(os.getcwd() + "/html/index.html")
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(f.read().encode())
        f.close()

    def zoo_shop_state(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write('<h2 style="text-align:left; color:green;">Pet Shop</h2>'.encode())
        self.wfile.write("<table>".encode())
        mu.acquire()
        try:
            localtime = time.asctime(time.localtime(time.time()))
            self.wfile.write('<tr style="color:blue;"><th colspan="3">{}</th><th></th><th></th><th></th></tr>'.format(localtime).encode())
            self.wfile.write('<tr><th> </th><th> </th><th> </th><th> </th><th> </th><th> </th></tr>'.encode())
            self.wfile.write('<tr><th>Gender</th><th>Name</th><th>Age(years)</th><th>Weight</th><th>Description</th><th>Species</th></tr>'.encode())
            for i in shop.get_animals():
                self.wfile.write('<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'.format(i.gender, i.name, round(i.age, 2), round(i.weight, 2), i.description, i.species).encode())
            self.wfile.write('<tr><th> </th><th> </th><th> </th><th> </th><th> </th><th> </th></tr>'.encode())
        except IndexError:
            self.wfile.write('<tr><th></th><th></th><th colspan="2">Pet Shop is empty</th><th></th><th></th></tr>'.encode())
        mu.release()
        self.wfile.write("</table>".encode())

    # def do_HEAD(self):
    #     self._set_headers()

    # def do_POST(self):
    #     # Doesn't do anything with posted data
    #     self._set_headers()
        # self.wfile.write("<html><body><h1>POST!</h1></body></html>".encode())


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
    httpd.server_close()


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
