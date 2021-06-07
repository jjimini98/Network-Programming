import smtplib
from email.message import EmailMessage
import imghdr


SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

sender = "jjimini98@gmail.com"
password = "fjgxsmbczbxrxpol"
mail_list = ["jjimini98@naver.com" , "lovers2019@kakao.com"]

msg = EmailMessage()
msg['Subject'] = "죠르디 사진이에오"
msg['From'] = sender
msg['To'] = ', '.join(mail_list)
msg.set_content("죠르디 사진이에오~.~")
msg.preamble= "You will not see this in a MIME-aware mail reader. \n"

with open("Final Exam\\Lecture 11\\facivon.png",'rb') as f:
   img_data = f.read()

msg.add_attachment(img_data, maintype='image', subtype=imghdr.what(None, img_data), filename= 'test.png')


s = smtplib.SMTP(SMTP_SERVER,SMTP_PORT)
s.ehlo()
s.starttls()
s.login(sender,password)
s.send_message(msg)
s.quit()