from socket import *

s = socket()
s.bind(('', 9000))
s.listen(10)
print("Server is running....")

while True:
    c, addr = s.accept()

    msg = c.recv(1024).decode()
    if not msg: break
    req = msg.split('\r\n')
    filename = req[0].split(" ")[1]


    try:
        if filename == "/":
            f = open("Daum.html", 'r', encoding='utf-8')
            mimeType = 'text/html'
            data = f.read()
        if "Daum_filesDaum_files/Daum_files/Daum_files/Daum_files/" in filename :
            f = open("png", 'rb')
            data = f.read()




        c.send(b"HTTP/1.1 200 OK\r\n")
        c.send(b"Content-Type : " + mimeType.encode() + b'\r\n')
        c.send(b"\r\n")


        if '/' in filename:
            c.send(data.encode())

        else: c.sendall(data)

    except:
        c.send(b"HTTP/1.1 404 Not Found \r\n")
        c.send(b"\r\n")
        c.send(b"<HTML><HEAD><TITLE> Not Found </TITLE></HEAD>")
        c.send(b"<BODY> Not Found </BODY></HTML>")

    c.close()
s.close()

