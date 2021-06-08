import paramiko
import getpass

IP = '106.10.57.110'
PORT = 1030

transport = paramiko.Transport((IP,PORT))

user = input('Username : ')
pwd = getpass.getpass('Password : ')
transport.connect(username=user, password=pwd)

sftp = paramiko.SFTPClient.from_transport(transport) #파일 전송을 위한 SFTPClient 생성 

# src_file_path = 'test/iot.txt'
# dst_file_path = src_file_path.split('/')[1] #iot.txt 파일만 가져옴 
# sftp.get(src_file_path,"Final Exam\\Lecture 11\\"+ dst_file_path) #서버에 있는 iot.txt 파일을 가져와서 저장 

src_file_path = 'Final Exam\\Lecture 11\\favicon.png'
dst_file_path = src_file_path
sftp.put(src_file_path,dst_file_path)

sftp.close()
transport.close() 