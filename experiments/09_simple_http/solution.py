#import SimpleHTTPServer
#import SocketServer
import get_sys_info
import threading
import time

from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8000

def my_thread_func(my_array, my_mutex):
    while True:
        a = time.strftime("%d %b %Y %H:%M:%S", time.gmtime())
        b = get_sys_info.get_cpu_usage()
        c = get_sys_info.get_mem()
        my_mutex.acquire()
        try:
            my_array.append([a,b,c])
            # print(a,b,c)
        except KeyboardInterrupt:
            return
        finally:
            my_mutex.release()

my_mutex = threading.Lock()
my_array = []

t1 = threading.Thread(target=my_thread_func, args=(my_array, my_mutex))
t1.start()

class S(BaseHTTPRequestHandler):

    def _set_headers(self):
        # Send response status code
        self.send_response(200)
        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        #get_sys_info.add_vals(self.my_array)
        # Write content that back to client
        self.wfile.write("<table>".encode())
        self.wfile.write('<tr><th>time</th><th>CPU</th><th>MEM</th></tr>'.encode())

        my_mutex.acquire()
        try:
            for i in my_array:
                self.wfile.write('<tr><td>{}</td><td>{}</td><td>{}</td></tr>'.format(i[0], i[1], i[2]).encode())
        finally:
            my_mutex.release()
        self.wfile.write("</table>".encode())

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write("<html><body><h1>POST!</h1></body></html>".encode())

Handler = S

httpd = HTTPServer(("", PORT), Handler)

print ("serving at port", PORT)
httpd.serve_forever()

t1.join()
