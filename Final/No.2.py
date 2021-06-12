from socket import *
import threading
import requests
from urllib import request

port = 8888
BUFFSIZE = 1024

print("Server is started ")

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(1)

def send_image(sock):
    conn, addr = sock.accept()

    msg = conn.recv(1024).decode()
    req = msg.split('\r\n')
    filename = req[0].split(" ")[1]

    if filename == "/iot.png":
        f = open("iot.png", 'rb')
        mimeType = "image/png"
        data = f.read()

    conn.send(b"HTTP/1.1 200 OK\r\n")
    conn.send(b"Content-Type : " + mimeType.encode() + b'\r\n')
    conn.send(b"\r\n")

    conn.close()
    sock.close()


th1 = threading.Thread(target=send_image, args=(sock,))
th1.start()
th1.join()