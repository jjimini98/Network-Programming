import socket

so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

addr = ('localhost', 9001)
so.connect(addr)
msg = so.recv(1024)
print(msg.decode())
# 본인의 이름을 문자열로 전송
so.send(b"Jimin Yoo")
# 본인의 학번을 수신 후 출력

so.close()