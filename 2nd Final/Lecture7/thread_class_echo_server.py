from socket import *
import threading

PORT = 2500
BUFSIZE = 1024

class ClientThread(threading.Thread):
    def __init__(self,sock):
        threading.Thread.__init__(self)
        self.sock = sock

    def run(self):
        while True:
            data = self.sock.recv(BUFSIZE)
            if not data :break
            print("Received Message : " , data.decode())
            self.sock.send(data)

        self.sock.close()

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('localhost', PORT))
sock.listen(5)

while True:
    conn, addr = sock.accept()
    print("Connected by : ", addr)
    th = ClientThread(conn)
    th.start()