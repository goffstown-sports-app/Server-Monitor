from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def send_email(html_content, recipient, subject):
    """Send an html file to someone

    Arguments:
        html_content {string} -- html to send
        recipient {string} -- who the email will be sent too
        subject {string} -- what the subject of the email should be
    """
    msg = MIMEMultipart()
    msg["From"] = "ghsappbot@gmail.com"
    msg["To"] = recipient
    with open("email_password.txt") as password_file:
        password = password_file.read().strip("\n")
    msg["Subject"] = subject
    body = html_content
    msg.attach(MIMEText(body, "html"))
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(msg["From"], password)
    server.sendmail(msg["From"], msg["To"], msg.as_string())
    server.quit()


# Testing
# import codecs
# file = codecs.open("test.html", "r")
# send_email(file.read(), "matthewgleich@gmail.com", "Testing Testing")
