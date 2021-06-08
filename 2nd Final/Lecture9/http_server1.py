from http.server import HTTPServer, BaseHTTPRequestHandler

Host = 'localhost'
port = 8080

class http_handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello IoT')

httpd = HTTPServer((Host, port), http_handler)
print("Serving HTTP on {} : {}".format(Host,port))
httpd.serve_forever()