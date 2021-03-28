import socket

# 서버 정보
se = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
se.bind(('',9001))
se.listen(2)

while True:
    client , addr = se.accept()
    print("Connection from", addr)
    client.send(b'Hello'+addr[0].encode())
    # #학생의 이름을 수신한 후 출력
   
    print(se.recv(1024).decode())
    #학생읳 학번을 정수형으로 전송

    client.close()