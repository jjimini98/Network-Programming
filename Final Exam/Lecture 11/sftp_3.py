import paramiko
import getpass

IP = '106.10.57.110'
PORT = 1030

filename = 'test.zip'
dirname = 'Final Exam\\Lecture 11'

CMD = 'zip -r' + filename + ' ' + dirname

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

user = input('Username : ')
pwd = getpass.getpass('Password : ')
ssh.connect(IP,PORT,username=user, password=pwd)

stdin, stdout, stderr = ssh.exec_command(CMD)

sftp = ssh.open_sftp()

sftp.get(dirname+filename, filename)
   
sftp.close()
ssh.close() 


