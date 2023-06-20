import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from_add = 'tomino99@gmail.com'
to_add = 'xsedlacekt@stuba.sk'
subject = "Mail with Python script - HTML tag"

msg = MIMEMultipart()
msg['From'] = from_add
msg['To'] = to_add
msg['Subject'] = subject

body = "<b>Hey there! Sending email with Python. </b>"
msg.attach(MIMEText(body, 'html'))
message = msg.as_string()

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('tomino99@gmail.com', '************')

server.sendmail(from_add, to_add, message)

server.quit()