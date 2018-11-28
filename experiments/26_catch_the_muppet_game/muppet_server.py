# -*- coding: utf-8 -*-
# muppet_server.py


from http.server import HTTPServer, BaseHTTPRequestHandler
from game_logic import *
from main import *
import json
import os
# import base64

PORT = 8000
# muppets = ["elmo.png", "big-bird.png", "oscar.png", "abby.png", "count-von-count.png", "bert.png", "kermit.png", "grover.png", "ernie.png", "cookie.png"]


class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.get_index_html("/html/index.html")

        if self.path == "/xhr_img.js":
            self.get_index_html("/html/xhr_img.js")

        if self.path == "/style.css":
            self.get_index_css("/css/style.css")

        if self.path == "/xhr_style.js":
            self.get_index_html("/html/xhr_style.js")

        if self.path == "/get_position":
            self.get_position()

        if self.path == "/favicon.ico":
            self.get_icon("/html/favicon.ico")

        if self.path == "/cookie.png":
            self.get_png("/images/cookie.png")

        if self.path == "/wallpaper.png":
            self.get_png("/images/wallpaper.png")
        if self.path == "/game_over.png":
            self.get_png("/images/game_over.png")
        if self.path == "/won.png":
            self.get_png("/images/won.png")
        if self.path == "/cactus.jpg":
            self.get_image("/images/cactus.jpg")

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

    def get_position(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        # muppet.animate()
        start()
        data = {'time': time.time()-start_time, 'pos': (muppet.pos[0], muppet.pos[1]), 'x': muppet.pos[0], 'y': muppet.pos[1], 'muppet': muppet.image}
        self.wfile.write(json.dumps(data, indent=4).encode())


def main():
    handler = Server
    httpd = HTTPServer(("localhost", PORT), handler)
    print("serving at port", PORT)
    httpd.serve_forever()


if __name__ == '__main__':
    main()
