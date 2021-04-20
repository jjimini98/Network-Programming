# 과제 4 이름과 정수 추가하기
from socket import *

server = socket(AF_INET, SOCK_STREAM)
server.bind(('',9000))
server.listen(2)
print("Server is running .... ")

while True:
    client, addr = server.accept()
    print("Accept from : " , addr)

    name = client.recv(1024).decode()
    print(name)
    client.send((20171458).to_bytes(4,'big'))

    client.close()