from socket import *
import threading
import time

s= socket(AF_INET,SOCK_STREAM)
s.bind(('',5555))
s.listen(1)


print("Server started")

clients = []

def sendtoclient(sock):
    conn, addr = s.accept()
    while True:
        data = conn.recv(1024)
        if 'quit' in data.decode():
            if addr in clients:
                print(addr, "exited")
                clients.remove(addr)
                continue

        if addr not in clients:
            print("New Client : ", addr)
            clients.append(addr)

        print(time.asctime()+ str(addr) + ':' + data.decode())



while True:
    th = threading.Thread(target=sendtoclient, args=(s,))
    th.start()
