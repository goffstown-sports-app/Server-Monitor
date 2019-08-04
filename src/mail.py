from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

msg = MIMEMultipart()
msg["From"] = "matthewgleich@gmai.com"
msg["To"] = "matthewgleich@icloud.com"
with open("email_password.txt") as password_file:
    password = password_file.read().strip("\n")
msg["Subject"] = "Hello World!"
body = "<h1>This works!! Yay!</h1>"
msg.attach(MIMEText(body, "html"))

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(msg["From"], password)
server.sendmail(msg["From"], msg["To"], msg.as_string())
server.quit()
