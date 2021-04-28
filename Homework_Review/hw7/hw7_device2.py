from socket import *
import random

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 9001))
s.listen(2)

while True:
    cl, addr = s.accept()
    print("Connect from :", addr)

    try:
        msg = cl.recv(1024).decode()  # request

    except:
        cl.send(b"Try again")

    else:
        if not msg:
            break
        if msg == "Request" :
            hb = random.randint(40, 140)
            walk = random.randint(2000,6000)
            cal = random.randint(1000,4000)

            s.send(b'HeartBeat = ', str(hb).encode(), b'Steps= ', str(walk).encode(), b'Cal = ', str(cal).encode())
cl.close()