import socket 

name = socket.gethostname()
print(name) #Jimin-Laptop

print(socket.gethostbyname(name)) #192.168.56.1


# 호스트 정보 관련 함수
print(socket.gethostbyname('homepage.sch.ac.kr'))

print(socket.gethostbyname_ex('homepage.sch.ac.kr'))

print(socket.gethostbyaddr('220.69.189.98'))

print(socket.getfqdn('220.69.189.98'))

print(socket.getfqdn('www.daum.net'))

print(socket.getfqdn('www.google.com')) 


print(socket.gethostbyname('homepage.sch.ac.kr'))

print(socket.gethostbyname_ex('homepage.sch.ac.kr'))

print(socket.gethostbyaddr('220.69.189.98'))

print(socket.getfqdn('www.daum.net'))

print(socket.getfqdn('www.google.com'))



# 여러 사이트의 IP주소를 확인하는 프로그램
import socket 


HOSTS = [
'www.sch.ac.kr',
'homepage.sch.ac.kr',
'www.daum.net',
'www.google.com',
'iot'
]


for host in HOSTS:
	try: print("{} : {}".format(host,socket.gethostbyname(host)))
	except socket.error as msg:
		print('{} : {}'.format(host,msg)) 