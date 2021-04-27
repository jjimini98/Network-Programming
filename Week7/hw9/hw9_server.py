from socket import *
import random
import time

port = 3333
BUFF_SIZE = 1024


sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('',port))
print("listening....")

reTx = 0


while True:
    sock.settimeout(None)
    data, addr = sock.recvfrom(BUFF_SIZE)
    if random.random() <= 0.5: continue
    else:
        sock.sendto(b'ack', addr)
        print("<-" , data.decode())
        msg = input("->")

    while reTx <= 3:
        resp = str(reTx) + ' ' + msg
        sock.settimeout(2)
        try:
            data, addr = sock.recvfrom(BUFF_SIZE)
        except timeout :
            reTx +=1
            continue
        else:
            sock.sendto(resp.encode(), addr)
