import socket

so = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
so.bind(('',9000))
so.listen(2)


while True:
    client, addr = so.accept()
    print("Connection From", addr)
    client.send(b'hello' + addr[0].encode())
    #이름 받기
    name = client.recv(1024)
    print(name.decode())
    #학번 전송
    client.send((20171458).to_bytes(4, 'big'))


    client.close()



