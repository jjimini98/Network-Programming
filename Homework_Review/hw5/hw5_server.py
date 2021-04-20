from socket import *

server = socket(AF_INET, SOCK_STREAM)
server.bind(('',9999))
server.listen(5)
print("waiting .... ")
client, addr = server.accept()
print("Connect from :", addr)

while True:
    msg = client.recv(1024)
    if not msg :
        break

    message = msg.decode()

    msg = message.split(" ")
    fi = int(msg[0])
    cal = msg[1]
    se = int(msg[2])
    if cal == "+":
        client.send(str((lambda x, y : x+y)(fi,se)).encode())
    elif cal == "-":
        client.send(str((lambda x, y : x-y)(fi,se)).encode())
    elif cal == "*":
        client.send(str((lambda x, y : x*y)(fi,se)).encode())
    elif cal == "/":
        client.send(str('%.1f' %(lambda x,y : x/y)(fi,se)).encode())

client.close()