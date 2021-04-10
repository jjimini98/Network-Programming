from socket import * 
import  mimetypes

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 80))
s.listen(10)

while True:
    c , addr = s.accept()

    data= c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')

    if not data: break #데이터가 없으면 없다는 메세지를 출력해야함 

    else: # 데이터가 있으면 파일을 읽기 시작

        if "index.html" in msg :

            c.send("HTTP/1.1 200 OK \r\n".encode())
            c.send("Content- Type + mimeType + \r\n".encode())
            c.send("\r\n".encode())

            with open("C:\\Users\\jimin\\vscode\\network_programming\\Week5\\hw6\\index.html", 'rb') as f:
                try:
                    data = f.read(1024) #1024바이트 읽는다
                    # f1 = open(r"C:\\Users\\jimin\\vscode\\network_programming\\Week5\\hw6\\iot.png", "rb")
                    # l1 = os.path.getsize(r"C:\\Users\\jimin\\vscode\\network_programming\\Week5\\hw6\\iot.png")
                    # m1 = f1.read(l1)
                    # s.send(m1)
                    
                    c.sendall(data)
    
      
                except Exception as ex:
                    print(ex)

            # mimeType = "image/png"
            # with open("C:\\Users\\jimin\\vscode\\network_programming\\Week5\\hw6\\iot.png", 'rb') as f:
            #     try:
            #         data = f.read(1024) #1024바이트 읽는다
            #         c.send(data)
      
            #     except Exception as ex:
            #         print(ex)


    
        # print(msg)
        # print(url)
    
c.close()

