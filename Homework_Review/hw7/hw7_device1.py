from socket import *
import random

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)


while True:
    cl , addr = s.accept()
    print("Connect from :", addr)

    try:
        msg = cl.recv(1024).decode() #request

    except :
        cl.send(b"Try again")

    else:
        if not msg :
            break
        if msg == "Request":
            temp = random.randint(0,40)
            humid = random.randint(0,100)
            lilum = random.randint(70,150)

            s.send(b'Temp = ',str(temp).encode(), b'Humid = ', str(humid).encode(), b'lilum = ', str(lilum).encode())
cl.close()