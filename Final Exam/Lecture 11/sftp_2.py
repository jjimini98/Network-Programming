import paramiko
import getpass

IP = '106.10.57.110'
PORT = 1030


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

user = input("Username : ")
pwd = getpass.getpass('Password : ')
ssh.connect(IP,PORT,username=user, password=pwd)

# sftp 객체 생성
sftp = ssh.open_sftp()

src_file_path = 'Final Exam\\Lecture 11\\hello.txt'
dst_file_path = 'test_jimin/' + src_file_path
print(dst_file_path)
sftp.put(src_file_path, dst_file_path)

src_file_path =  dst_file_path
dst_file_path = 'iot.txt'
sftp.get(src_file_path,dst_file_path)

sftp.close()
ssh.close() 