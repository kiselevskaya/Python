A simple http server

Run function that puts system information to the list <my_array> by thread. Handler class sets headers, send <GET> request to receive information from the list <my_array> as table with time, <CPU> and MEM, sends <HEAD> and <POST> requests. When run the script, the server will start on port <8000>.
To check in the browser put <http://localhost:PORT>.

'''
def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()
'''
