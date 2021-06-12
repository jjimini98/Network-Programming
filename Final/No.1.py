from http.server import BaseHTTPRequestHandler, HTTPServer

class http_handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.route()

    def route(self):
        if self.path=='/':
            self.send_image()

    def send_image(self):
        self.send_response(200)
        self.send_header("Content-type","image/png")
        self.end_headers()
        with open("iot.png", "rb") as p:
            pic = p.read()
            self.wfile.write(pic)


httpd = HTTPServer(('localhost',8888),http_handler)
print("Serving HTTP on {}:{}".format('localhost',8888))
httpd.serve_forever()