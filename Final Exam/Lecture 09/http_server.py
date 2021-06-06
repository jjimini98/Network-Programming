from http.server import HTTPServer, BaseHTTPRequestHandler

class Myhandler(BaseHTTPRequestHandler):
   def do_GET(self):
      self.send_response(200) #상태코드를 클라이언트에게 보냄
      self.end_headers()
      self.wfile.write("<h1>hello world</h1>".encode())

httpd = HTTPServer(('localhost',8000),Myhandler)

httpd.serve_forever()
