import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 80))
server.listen(2)

while True:
    c, addr = server.accept()
    data= c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')[0][4:15]

    if req == "/index.html":

        f = open("index.html", 'r', encoding='utf-8')
        mimeType = 'text/html'
        c.send("HTTP/1.1 200 OK \r\n".encode())
        c.send("Cotent-Type : ".encode() + mimeType.encode() + '\r\n'.encode())
        c.send("\r\n".encode())
        m = c.recv(2038).decode()
        print(m)
        #사진보내기
        file = open("iot.png",'rb')

        mimeType ='image/png'
        c.send("HTTP/1.1 200 OK \r\n".encode())
        c.send("Cotent-Type : ".encode()+ mimeType.encode() + '\r\n'.encode())
        c.send("\r\n".encode())

        while file:
            img = c.send(file.read())

        file.close()
