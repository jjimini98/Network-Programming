import binascii
import socket
import sys

for string_address in ['114.71.220.95']: # 굳이 for문을 써야했을까?ㅠ
	packed = socket.inet_aton(string_address) #문자열 주소를 4바이트 bytes 객체로 변환 
	print("Original : " , string_address) 
	print("Packed : " , binascii.hexlify(packed))  # binascii.hexlify() :bytes 객체로 변환한 값을 보기 좋게 변경할 때 사용함 
	print("Unpacked : ", socket.inet_ntoa(packed))
