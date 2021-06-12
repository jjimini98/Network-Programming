import select
from socket import *
import random

s_list = []
s_sock = socket(AF_INET,SOCK_STREAM)
s_sock.bind(('',9999))
s_sock.listen(5)

s_list.append(s_sock)
while True:
    r_sock , w_sock, e_sock = select.select(s_list, [], [])

    for r in r_sock:
        if r == s_sock:
            c_sock,addr = s_sock.accept()
            s_list.append(c_sock)
            print("Connected from {}".format(addr))

        else:
            data = r.recv(1024)
            if not data :
                r.close()
                s_list.remove(r)
                continue

            elif data.decode() == "1":
                temp = random.randint(0, 40)
                msg = "Temp=" + str(temp)
                c_sock.send(msg.encode())

            elif data.decode() == "2":
                humid = random.randint(0, 100)
                msg = "Humid=" + str(humid)
                c_sock.send(msg.encode())