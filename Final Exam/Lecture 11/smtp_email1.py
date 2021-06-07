import smtplib
from email.message import EmailMessage

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

sender = 'jjimini98@gmail.com' #보내는 사람
recipient = 'jjimini98@naver.com' #받는사람 
password = "fjgxsmbczbxrxpol"

msg = EmailMessage()
msg['Subject'] = "이메일 테스트임미다~"
msg['From'] =sender
msg['To'] = recipient
text = "안뇽 지희"
msg.set_content(text)

s = smtplib.SMTP(SMTP_SERVER,SMTP_PORT)
s.ehlo()
s.starttls()
s.login(sender,password)
s.send_message(msg)
s.quit()