# html 메일 전송하기 

import smtplib 
from email.message import EmailMessage

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

sender = 'jjimini98@gmail.com'
recipient = 'jjimini98@naver.com'
password = 'fjgxsmbczbxrxpol'

msg = EmailMessage()
msg['subject'] = "HTML 메세지입니다. 확인 부탁드려요"
msg['From'] = sender
msg['To'] = recipient
content_id = 'my_image'
msg.add_alternative('''
<html>
   <head></head>
   <body>
   <p> 안녕하세요 저는 유지민입니다 </p>
   <p> 아래 사이트 확인 부탁드립니다. </p>
   <p> 
      <a href=https://growingarchive.tistory.com/>
         지민이네 블로그 ~ 
      </a>
   </p>
   <p> 감사합니다 </p>
   <img src="cid:{cid}" />
   </body>
</html>
'''.format(cid=content_id), subtype = 'html')


with open('Final Exam\\Lecture 11\\facivon.png','rb') as img:
   msg.get_payload()[0].add_related(img.read(),maintype='image', subtype='png', cid= content_id)

with open('outgoing.msg','wb') as f:
   f.write(bytes(msg))

s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
s.ehlo()
s.starttls()
s.login(sender, password)
s.send_message(msg)
s.quit() 