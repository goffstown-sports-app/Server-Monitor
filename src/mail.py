import json
import smtplib

with open("gmail_creds.json") as gmail_creds:
    content = json.load(gmail_creds)
email_address = content["email-address"]
email_password = content["email-password"]

with smtplib.SMTP('stmp.gmail.com', 8080) as smtp:
    smtp.ehlo()
    smtp.startssl()
    smtp.ehlo()

    smtplib.login(email_address, email_password)
    subject = "Grab dinner this weekend?"
    body = "How about dinner at 6pm this Saturday?"

    msg = f"Subject: {subject}\n\n{body}"

    smtp.sendmail(email_address, "matthewgleich@gmail.com", msg) 