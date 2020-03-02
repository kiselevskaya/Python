

from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import asyncio
import threading
import websockets
import urllib
from main_logic import *


main_logic = MainLogic()


class HttpHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        path = self.path
        if path == "/":
            path = "/weight_for_weight.html"

        if path.startswith("/register"):
            return self.process_register_form(path)

        if urllib.parse.urlparse(path).path == "/game":
            return self.process_next_page(path)

        self.get_static(path)

    def process_register_form(self, path):
        parsed_path = urllib.parse.urlparse(path)
        query = urllib.parse.parse_qs(parsed_path.query)
        if 'username' in query:
            username = query['username'][0]
            return self.try_to_register_new_user(username)
        return self.return_err("no username parameter")

    def try_to_register_new_user(self, username):
        password = main_logic.add_user(username)
        if password is not None:
            return self.redirect("game?username=" + username + "&password=" + password)
        return self.return_err("user cannot be registered")

    def redirect(self, path):
        self.send_response(303)
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        self.send_header('Location', path)
        self.end_headers()

    def process_next_page(self, path):
        parsed_path = urllib.parse.urlparse(path)
        query = urllib.parse.parse_qs(parsed_path.query)
        if 'username' in query and 'password' in query:
            username = query['username'][0]
            password = query['password'][0]
            if main_logic.check_user(username, password):
                self.get_static("/game.html")
                return
        return self.return_err("username or password is bad")

    def get_static(self, path):
        mode = "r"
        if path == "/favicon.png":
            mode = "rb"
        if path.endswith('.css'):
            mimetype = 'text/css'
        elif path.lower().endswith('.png'):
            mimetype = 'image/png'
            mode = 'rb'
        elif path.lower().endswith('.jpg'):
            mimetype = 'image/jpg'
            mode = 'rb'
        elif path.endswith('.js'):
            mimetype = 'application/javascript'
            path = '/html/' + path
        else:
            mimetype = 'text/html'
            path = '/html/' + path
        try:
            f = open(os.getcwd() + path, mode)
            self.send_response(200)
            self.send_header('Content-Type', mimetype)
            self.end_headers()
            if mode == "r":
                self.wfile.write(f.read().encode())
            else:
                self.wfile.write(f.read())
            f.close()
        except OSError as e:
            self.return_err(path=path, e=e)
        except UnicodeDecodeError as e:
            self.return_err(path=path, e=e)

    def return_err(self, message=None, path=None, e=None):
        if e is not None:
            print(e, " for file " + path)
        self.send_response(404)
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        if message is not None:
            self.wfile.write(message.encode())
        self.wfile.write("<hr/><a href=\"/\">Log off</a>".encode())


async def process_wsc_connection(websocket, path):
    parsed_path = urllib.parse.urlparse(path)
    query = urllib.parse.parse_qs(parsed_path.query)
    if 'username' in query and 'password' in query:
        username = query['username'][0]
        password = query['password'][0]
        if main_logic.check_user(username, password):
            await main_logic.process_websocket(username, websocket)
        print("user " + username + " logged off")
    websocket.close()


def http_server():
    port = 80
    httpd = HTTPServer(('0.0.0.0', port), HttpHandler)
    print('serving http at port', port)
    httpd.serve_forever()


def websocket_server():
    port = 6789
    print('serving websocket at port', port)
    return websockets.serve(process_wsc_connection, '0.0.0.0', port)


def start_http():
    event_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(event_loop)
    event_loop.run_until_complete(http_server())
    event_loop.run_forever()


def start_websocket():
    ws_event_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(ws_event_loop)
    ws_event_loop.run_until_complete(websocket_server())
    ws_event_loop.run_forever()


def main():
    t_http = threading.Thread(target=start_http)
    t_websocket = threading.Thread(target=start_websocket)
    t_http.daemon = True
    t_websocket.daemon = True
    t_http.start()
    t_websocket.start()
    t_http.join()
    t_websocket.join()


if __name__ == '__main__':
    main()
