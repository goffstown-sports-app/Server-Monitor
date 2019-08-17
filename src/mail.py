from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import codecs

# msg = MIMEMultipart()
# msg["From"] = "ghsappbot@gmail.com"
# msg["To"] = "matthewgleich@gmail.com"
# with open("email_password.txt") as password_file:
#     password = password_file.read().strip("\n")
# msg["Subject"] = "Hello World!"
# body = "<h1>This works!! Yay!</h1>"
# msg.attach(MIMEText(body, "html"))

# server = smtplib.SMTP("smtp.gmail.com", 587)
# server.starttls()
# server.login(msg["From"], password)
# server.sendmail(msg["From"], msg["To"], msg.as_string())
# server.quit()

def read_html_file(file_name):
    """Reads an HTMl file and saves each line in an array as a string
    
    Arguments:
        file_name {str} -- path to the file, if in current directory then just the file name
    
    Returns:
        list -- list of all the lines
    """
    file = codecs.open(file_name)
    file_contents = file.read()
    lines = file_contents.split("\n")
    return lines

# Testing:
# print(read_html_file("problem.html"))
