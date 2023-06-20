import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send(filename):
    from_add = 'tomino99@gmail.com'
    to_add = 'xsedlacekt@stuba.sk'
    subject = "Finance Stock Report"

    msg = MIMEMultipart()
    msg['From'] = from_add
    msg['To'] = to_add
    msg['Subject'] = subject

    body = "<b>Todays finance stock report!</b>"
    msg.attach(MIMEText(body, 'html'))

    my_file = open(filename, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(my_file.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename= ' + filename)
    msg.attach(part)

    message = msg.as_string()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('tomino99@gmail.com', '**********')

    server.sendmail(from_add, to_add, message)

    server.quit()