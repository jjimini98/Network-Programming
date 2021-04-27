import socket
import random

#클라이언트에서 서버로 보낼 때 손실 발생
# 서버는 40%의 확률로 받지 못함
# 재전송은 1초 간격으로 총 3번

port = 2500
BUFFSIZE = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input('Enter a message: ')
    if msg == 'q': break

    if random.randint(1, 10) <= 4:
        print('Packet lost!')
        continue
    print('Packet is success')
    sock.sendto(msg.encode(),('localhost',port))
    print('Received: ', msg,('localhost', port))




sock.close()





# for i in range(4):
#     count = 0
#     time  = 1  # 1초를 의미
#     while True:
#         msg = input('Enter a message: ')
#         if msg == 'q':
#             break
#         sock.sendto(msg.encode(), ('localhost', port))
#         try :
#             data, addr = sock.recvfrom(BUFFSIZE)
#             print('Server says: ', data.decode())
#         except socket.timeout:
#             count +=1  # 대기시간 2배 증가
#             if count == 4:  # 최대 대기시간 초과
#                 break
#             else:
#                 print('Server says: ', data.decode())
#             break
# sock.close()