import smtplib
from email.message import EmailMessage
import zipfile
import os

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

sender = 'jjimini98@gmail.com'
recipient = 'jjimini98@naver.com'
password = 'fjgxsmbczbxrxpol'

zf_name = 'email.zip'
folder = 'Final Exam\\Lecture 11'

zf = zipfile.ZipFile(zf_name, 'w')
print("Zipping current dir", folder)
for dirs , subdirs, files in os.walk(folder):
   zf.write(dirs)
   for file in files:
      zf.write(os.path.join(dirs,file))

zf.close()


msg = EmailMessage()
msg['Subject'] = "압축파일과 함께 보내는 메일~"
msg['From']  = sender
msg['To'] = recipient


with open(zf_name, 'rb') as f:
   msg.add_attachment(f.read(), maintype='application', subtype='zip', filename='email.zip')


s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
s.ehlo()
s.starttls()
s.login(sender,password)
s.send_message(msg)
s.quit() 