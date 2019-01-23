from http.server import HTTPServer, BaseHTTPRequestHandler
from game_logic import *
import asyncio
import os
import urllib
import websockets
import threading

game_logic = GameLogic()


class HttpHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        path = self.path
        if path == "/":
            path = "/index.html"

        if path.startswith("/register"):
            return self.process_register(path)

        if urllib.parse.urlparse(path).path == "/game":
            return self.process_game(path)

        self.get_static(path)

    def process_register(self, path):
        parsed_path = urllib.parse.urlparse(path)
        query = urllib.parse.parse_qs(parsed_path.query)
        if 'username' in query:
            username = query['username'][0]
            return self.try_to_register_new_user(username)
        return self.return_err("no username parameter")

    def try_to_register_new_user(self, username):
        password = game_logic.add_user(username)
        if password is not None:
            return self.redirect("game?username=" + username + "&password=" + password)
        return self.return_err("user cannot be registered")

    def process_game(self, path):
        parsed_path = urllib.parse.urlparse(path)
        query = urllib.parse.parse_qs(parsed_path.query)
        if 'username' in query and 'password' in query:
            username = query['username'][0]
            password = query['password'][0]
            if game_logic.check_user(username, password):
                self.get_static("/game.html")
                return
        return self.return_err("username or password is bad")

    def redirect(self, path):
        self.send_response(303)
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        self.send_header('Location', path)
        self.end_headers()

    def get_static(self, path):
        mode = "r"
        if path == "/favicon.ico":
            mode = "rb"
        try:
            f = open(os.getcwd() + "/html/" + path, mode)
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
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


async def process_user_connection(websocket, path):
    parsed_path = urllib.parse.urlparse(path)
    query = urllib.parse.parse_qs(parsed_path.query)
    if 'username' in query and 'password' in query:
        username = query['username'][0]
        password = query['password'][0]
        if game_logic.check_user(username, password):
            await game_logic.process_websocket(username, websocket)
            # await game_logic.get_list_of_users(websocket)
        print("user " + username + " logged off")
    websocket.close()


def http_server():
    port = 8081
    httpd = HTTPServer(('localhost', port), HttpHandler)
    print('serving http at port', port)
    httpd.serve_forever()


def websocket_server():
    port = 6789
    print('serving websocket at port', port)
    return websockets.serve(process_user_connection, '127.0.0.1', port)


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
    t_http.daemon = True
    t_websocket = threading.Thread(target=start_websocket)
    t_websocket.daemon = True
    t_http.start()
    t_websocket.start()
    t_http.join()
    t_websocket.join()


if __name__ == '__main__':
    main()
