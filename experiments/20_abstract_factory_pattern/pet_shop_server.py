# -*- coding: utf-8 -*-
# pet_shop_server.py

from http.server import HTTPServer, BaseHTTPRequestHandler
from main import *
import time


shop = create_shop()
PORT = 8000


class Server(BaseHTTPRequestHandler):
    def _set_headers(self):
        # Send response status code
        self.send_response(200)
        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        # Write content that back to client
        self.wfile.write('<head><meta http-equiv="refresh" content="10"></head>'.encode())
        self.wfile.write('<h2 style="text-align:left; color:green;">Pet Shop</h2>'.encode())
        self.wfile.write("<table>".encode())
        try:
            localtime = time.asctime(time.localtime(time.time()))
            self.wfile.write('<tr style="color:blue;"><th colspan="3">{}</th><th></th><th></th><th></th></tr>'.format(localtime).encode())
            self.wfile.write('<tr><th> </th><th> </th><th> </th><th> </th><th> </th><th> </th></tr>'.encode())
            self.wfile.write('<tr><th>Gender</th><th>Name</th><th>Age(years)</th><th>Weight</th><th>Description</th><th>Species</th></tr>'.encode())
            for i in shop.get_animals():
                self.wfile.write('<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'.format(i.gender, i.name, round(i.age, 2), round(i.weight, 2), i.description, i.species).encode())
            self.wfile.write('<tr><th> </th><th> </th><th> </th><th> </th><th> </th><th> </th></tr>'.encode())
            shop.ticker()
        except IndexError:
            self.wfile.write('<tr><th></th><th></th><th colspan="2">Pet Shop is empty</th><th></th><th></th></tr>'.encode())
        self.wfile.write("</table>".encode())

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write("<html><body><h1>POST!</h1></body></html>".encode())


Handler = Server

httpd = HTTPServer(("localhost", PORT), Handler)

print("serving at port", PORT)
while len(shop.get_animals()) > 0:
    httpd.serve_forever()
else:
    httpd.server_close()
