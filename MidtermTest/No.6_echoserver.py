import socket

port = 2500
BUFFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))
print("Server is running .... ")

for i in range(4):
    count = 0
    time  = 1  # 1초를 의미
    while True:
        try :
            data, addr = sock.recvfrom(BUFFSIZE)
            print('Server says: ', data.decode())
        except socket.timeout:
            count +=1  # 대기시간 2배 증가
            if count == 4:  # 최대 대기시간 초과
                break
            else:
                print('Server says: ', data.decode())
            break
sock.close()