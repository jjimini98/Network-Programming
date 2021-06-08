from socket import *
import threading

PORT = 2500
BUFSIZE = 1024

def echoTask(sock):
    while True:
        data = sock.recv(BUFSIZE)
        if not data : break
        print("Received Message : ", data.decode())
        sock.send(data)

    sock.close()

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('localhost',PORT))
sock.listen(5)

while True:
    conn, addr = sock.accept()
    print("Connected by :", addr)
    th = threading.Thread(target=echoTask, args=(conn,))
    th.start()
