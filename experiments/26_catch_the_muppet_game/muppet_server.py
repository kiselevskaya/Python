# -*- coding: utf-8 -*-
# muppet_server.py


from http.server import HTTPServer, BaseHTTPRequestHandler
from game_logic import *
from main import *
import json
import os
# import base64

PORT = 8000
muppets = ["elmo.png", "big-bird.png", "oscar.png", "abby.png", "count-von-count.png", "bert.png", "kermit.png", "grover.png", "ernie.png", "cookie.png"]
other_png = ["wallpaper.png", "game_over.png", "won.png", "cactus.jpg"]


class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.get_index_html("/html/index.html")
        if self.path == "/style.css":
            self.get_index_css("/css/style.css")
        if self.path == "/favicon.ico":
            self.get_icon("/html/favicon.ico")
        if self.path == "/xhr_img.js":
            self.get_index_html("/html/xhr_img.js")
        if self.path == "/xhr_style.js":
            self.get_index_html("/html/xhr_style.js")
        if self.path[1:] in other_png:
            self.get_image("/images" + self.path)
        if self.path[1:] in muppets:
            self.get_png("/images" + self.path)

        if self.path == "/get_muppet":
            self.get_muppet()
        if self.path == "/get_score":
            self.get_score()
        if self.path == "/get_logs":
            self.get_logs()
        if self.path == "/get_level":
            self.get_level()

    def get_index_html(self, path):
        f = open(os.getcwd() + path)
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(f.read().encode())
        f.close()

    def get_index_css(self, path):
        f = open(os.getcwd() + path)
        self.send_response(200)
        self.send_header('Content-Type', 'text/css')
        self.end_headers()
        self.wfile.write(f.read().encode())
        f.close()

    def get_icon(self, path):
        f = open((os.getcwd() + path), 'rb')
        self.send_response(200)
        self.send_header('Content-Type', 'image/x-icon')
        self.end_headers()
        self.wfile.write(f.read())
        f.close()

    def get_image(self, path):
        f = open((os.getcwd() + path), 'rb')
        self.send_response(200)
        self.send_header('Content-Type', 'image/jpg')
        self.end_headers()
        self.wfile.write(f.read())
        f.close()

    def get_png(self, path):
        f = open((os.getcwd() + path), 'rb')
        self.send_response(200)
        self.send_header('Content-Type', 'image/png')
        self.end_headers()
        self.wfile.write(f.read())
        f.close()

    def get_muppet(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        start()
        data = {'x': muppet.pos[0], 'y': muppet.pos[1], 'muppet': muppet.image}
        self.wfile.write(json.dumps(data, indent=4).encode())

    def get_score(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        start()
        data = {'caught': score[0], 'missed': score[1]}
        self.wfile.write(json.dumps(data, indent=4).encode())

    def get_logs(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        start()
        data = {'logs': '\n'.join(logs)}
        self.wfile.write(json.dumps(data, indent=4).encode())

    def get_level(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        start()
        data = {'level': "LEVEL " + str(level)}
        self.wfile.write(json.dumps(data, indent=4).encode())


def main():
    handler = Server
    httpd = HTTPServer(("localhost", PORT), handler)
    print("serving at port", PORT)
    httpd.serve_forever()


if __name__ == '__main__':
    main()
