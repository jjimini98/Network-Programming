from socket import *

clien = socket(AF_INET, SOCK_STREAM)
clien.connect(('localhost', 9999))

while True:
    try:
        sentence = input("계산식을 입력하세요 >>")
    except:
        print("Connection closed")
    else:
        if sentence == "q":
            break
        clien.send(sentence.encode())
        print("Result: ", clien.recv(1024).decode())

clien.close()