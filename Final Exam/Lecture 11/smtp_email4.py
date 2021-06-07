import smtplib
from email.message import EmailMessage
from openpyxl import load_workbook

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

sender = 'jjimini98@gmail.com'
password = 'fjgxsmbczbxrxpol'

load_wb = load_workbook("Final Exam\\Lecture 11\\email_list.xlsx")


load_ws = load_wb['Sheet']
for row in load_ws.rows:
   recipient = row[0].value

   msg = EmailMessage()
   msg['Subject'] = '헬로~ 이것은 엑셀파일로 보내는 이메일이에용'
   msg['From'] = sender
   msg.set_content("조금만 힘내용 오늘 내일만 지나면 넽웤  시험 끝!  잘볼 수 있다구용~")
   msg['To']  = recipient

   s = smtplib.SMTP(SMTP_SERVER,SMTP_PORT)
   s.ehlo()
   s.starttls()
   s.login(sender,password)
   s.send_message(msg)
   s.quit()