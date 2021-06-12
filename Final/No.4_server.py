import selectors
from socket import *
import random

s = socket(AF_INET,SOCK_STREAM)
s.bind(('',9999))
s.listen(5)

sel = selectors.DefaultSelector()

def accept(sock, mask):
    conn, addr = sock.accept()
    print("Connected from" , addr)
    sel.register(conn,selectors.EVENT_READ, read)


def read(conn,mask):
    data = conn.recv(1024)
    if not data:
        sel.unregister(conn)
        conn.close()
        return

    elif data.decode() == "1":
        temp = random.randint(0, 40)
        msg = "Temp="+str(temp)
        conn.send(msg.encode())

    elif data.decode() == "2":
        humid = random.randint(0, 100)
        msg = "Humid=" + str(humid)
        conn.send(msg.encode())



sel.register(s, selectors.EVENT_READ, accept)
while True:
    events = sel.select()
    for key,mask in events:
        callback = key.data
        callback(key.fileobj, mask)
