import socket

sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
# address = ('localhost', 9000)
sock.connect(('localhost', 9000))

sock.send(b'jimin Yoo')

# 이름 받기
msg = sock.recv(1024)
print(msg.decode())

# 학번 출력  
id=sock.recv(1024)
print(int.from_bytes(id, 'big'))


sock.close()