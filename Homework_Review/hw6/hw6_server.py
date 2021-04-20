from socket import *

s = socket()
s.bind(('', 81))
s.listen(10)
print("Server is running....")

while True:
    c, addr = s.accept()

    msg = c.recv(1024).decode()

    if not msg: break
    req = msg.split('\r\n')
    filename = req[0].split(" ")[1] #/index.html

    try:
        if 'index.html'in filename:
            f = open("C:\\Users\\jimin\\PycharmProjects\\NetworkProgramming\\Week5\\hw6\\index.html", 'r', encoding='utf-8')
            mimeType = 'text/html'
            data = f.read()
        elif filename =="/iot.png":
            f = open("C:\\Users\\jimin\\PycharmProjects\\NetworkProgramming\\Week5\\hw6\\iot.png",'rb')
            mimeType = "image/png"
            data = f.read()
        elif filename =="/favicon.ico":
            f = open("C:\\Users\\jimin\\PycharmProjects\\NetworkProgramming\\Week5\\hw6\\favicon.ico", 'rb')
            mimeType = 'image/x-icon'
            data = f.read()

        c.send(b"HTTP/1.1 200 OK\r\n")
        c.send(b"Content-Type : " + mimeType.encode() + b'\r\n')
        c.send(b"\r\n")

        if 'index.html' in filename:
            c.send(data.encode())
        else: c.sendall(data)
    except:
        # 웹페이지를 못열겠다면
        c.send(b"HTTP/1.1 404 Not Found \r\n")
        c.send(b"\r\n")
        c.send(b"<HTML><HEAD><TITLE> Not Found </TITLE></HEAD>")
        c.send(b"<BODY> Not Found </BODY></HTML>")

    c.close()
s.close()
