import time
import smtplib
from email.message import EmailMessage
import paramiko
import getpass

bufsize = 1024

cli = paramiko.SSHClient()
cli.set_missing_host_key_policy(paramiko.AutoAddPolicy())

user = input("Username : ")
pwd = getpass.getpass("Password : ")

cli.connect('106.10.57.110', 1030, username=user, password=pwd)
channel = cli.invoke_shell()

channel.send('mkdir 20171458\n')
time.sleep(0.5)
channel.send('cd 20171458\n')
time.sleep(0.5)
channel.send('echo iot > iot.txt\n')


####
filename = '20171458.zip'
dirname = '/root/20171458'
CMD = 'zip -r ' + filename + ' ' + dirname

stdin , stdout , stderr = cli.exec_command(CMD)

sftp = cli.open_sftp()
sftp.get(filename,filename)

sftp.close()
cli.close()


####

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

sender = 'jjimini98@gmail.com'
recipient = 'daeheekim@sch.ac.kr'
password = 'fjgxsmbczbxrxpol'

msg = EmailMessage()
msg['Subject'] = "20171458.zip"
msg['From'] = sender
msg['To']= recipient
msg.set_content("한학기 동안 정말 감사했습니다!")
msg.preamble = "You will not see this in a MIME-aware mail reader. \n"

zipfile = '20171458.zip'
with open(zipfile, 'rb') as f:
    msg.add_attachment(f.read(), maintype = 'application', subtype= 'zip', filename = '20171458.zip')


s = smtplib.SMTP(SMTP_SERVER,SMTP_PORT)
s.ehlo()
s.starttls()
s.login(sender,password)
s.send_message(msg)
s.quit()

