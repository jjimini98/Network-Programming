from socket import *
import time

clients = []

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 2500))

print("Server started")

while True :
    data , addr = s.recvfrom(1024)
    if 'quit' == data.decode():
        if addr in clients:
            print(addr ,"exited")
            clients.remove(addr)
            continue

    if addr not in clients:
        print("New Client" , addr)
        clients.append(addr)

    print(time.asctime() + str(addr) + ':' + data.decode())

    for client in clients:
        if client != addr :
            s.sendto(data, client)
