from socket import *
import time
import random

c = socket(AF_INET, SOCK_STREAM)

while True:
    choice =  input()

    if choice == "1":
        c.connect(('localhost', 9000))
        c.send(b'Request')
        result = c.recv(1024).decode()
        f = open("data.txt",'w')
        for _ in range(5):
            f.write (time.strftime('%c', time.localtime(time.time())))
            f.write(": Device 1 :")
            f.write(result)
            f.write("\n")

        f.close()