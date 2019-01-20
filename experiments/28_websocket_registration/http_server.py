from http.server import HTTPServer, BaseHTTPRequestHandler
from game_logic import *
import asyncio
import os
import urllib

game_logic = GameLogic()


class HttpHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        path = self.path
        if path == "/":
            path = "/index.html"

        if path.startswith("/register"):
            return self.process_register(path)

        if path.startswith("/game"):
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


def http_server():
    port = 8081
    httpd = HTTPServer(('localhost', port), HttpHandler)
    print('serving at port', port)
    httpd.serve_forever()


def start_http(event_loop2):
    event_loop2.run_until_complete(http_server())


def main():
    event_loop = asyncio.get_event_loop()
    start_http(event_loop)
    event_loop.run_forever()


if __name__ == '__main__':
    main()
