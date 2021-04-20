from socket import *

server = socket(AF_INET, SOCK_STREAM)
server.bind(('',9999))
server.listen(5)
print("waiting .... ")

while True:
    # 여기다가 accept하면 에러가남
    # print("Result: ", clien.recv(1024).decode())
    # ConnectionAbortedError: [WinError 10053] 현재 연결은 사용자의 호스트 시스템의 소프트웨어의 의해 중단되었습니다
    client , addr = server.accept()
    print("Connect from :" , addr)

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