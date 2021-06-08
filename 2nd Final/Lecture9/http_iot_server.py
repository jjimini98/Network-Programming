from http.server import HTTPServer,BaseHTTPRequestHandler
from urllib import parse

class http_handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.route()

    def do_Post(self):
        self.route()

    def route(self):
        parsed_path = parse.urlparse(self.path)
        real_path = parsed_path.path
        if real_path == "/":
            self.send_html()

        elif real_path == "/button":
            self.proc_query()

        elif real_path == "/form_get":
            self.proc_query()

        elif real_path == "/form_post":
            self.proc_query_post()
        else: self.response(404, "<h1>NOT FOUND</h1>")

    def send_html(self):
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()
        with open("index_get.html","r") as f:
            msg = f.read()
            self.wfile.write(msg.encode())

    def proc_query(self):
        parsed_path = parse.urlparse(self.path)
        print(parsed_path)
        query = parsed_path.query
        print(query)
        parsed_query = parse.parse_qs(query)
        print(parsed_query)
        status = parsed_query['status'][0]
        if status == "on":
            message = '<h2>LED in IoT Device is now turned on</h2>'
        elif status == "off":
            message = "<h2>LED in IoT Device is now turned off</h2>"
        else: message = "<h2>Wrong status</h2>"

        self.response(200,message)

    def proc_query_post(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length).decode()
        print(body)
        parsed_body = body.split("=")
        print(parsed_body)
        status = parsed_body[1]

        if status == "on":
            message = '<h2>LED in IoT Device is now turned on</h2>'
        elif status == "off":
            message = "<h2>LED in IoT Device is now turned off</h2>"

        else: message = "<h2>Wrong status</h2>"

        self.response(200,message)

    def response(self,status_code, body):
        self.send_response(status_code)
        self.send_header("Content-type","text/html")
        self.end_headers()
        self.wfile.write(body.encode())

info = ('localhost',8080)
httpd = HTTPServer(info,http_handler)
print("Serving HTTP on {}:{}".format(info[0],info[1]))
httpd.serve_forever()