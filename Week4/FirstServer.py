import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM ) #IPv4 , TCP

s.bind(('', 9000))  #ip와 port번호는 튜플 형태로 input
#ip자리에 '' 을 넣으면 내가 가지고 있는 모든 ip주소에 9000번 포트를 바인딩

s.listen(2) # 서버에 동시에 접속할 수 있는 클라이언트 개수 ( 여기선 작게 2개 )

while True:
	client, addr = s.accept() # client 변수에 클라이언트와 접속할 수 있는 socket생성
	#accept()도 블로킹 후 기다리는 함수
	print("Connection From" , addr)
	client.send(b"hello " + addr[0].encode())
	# b 또는 .encode()를 쓰면 문자열을 byte형태로 변환해준다.
	# addr[0] 에는 ip주소가 들어감 / addr[1] 에는 포트 번호가 들어감
	client.close()  # socket 닫기