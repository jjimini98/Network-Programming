import zipfile

zf = zipfile.ZipFile('Final Exam\\Lecture 11\\Sample.zip', 'w')
zf.write('Final Exam\\Lecture 11\\email_list.xlsx')
zf.write('Final Exam\\Lecture 11\\facivon.png')
zf.close()


uzf = zipfile.ZipFile('Final Exam\\Lecture 11\\sample.zip','r')
uzf.extractall()
