from socket import *
import random

port = 3333
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.connect(('localhost', port))


while True :
    # msg = input("->")
    reTx = 0
    msg = input("->")
    resp = str(reTx) + ' ' + msg
    sock.sendto(resp.encode(), ('localhost', port))
    sock.settimeout(2)

    while reTx <= 3:
        sock.settimeout(None)
        try:
            data,addr = sock.recvfrom(BUFF_SIZE)

        except timeout:
            reTx += 1
            continue
        else:
            print("<-", data.decode())
            break




