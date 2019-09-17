import sys
import codecs

sys.path.append("..")
import mail

def test_send_email():
    """Tests for the send email function
    """
    html_file = codecs.open("test.html", "r")
    instance = mail.send_email(html_file.read(), "ghsappbot@gmail.com", "CI TEST")
    html_file.close()
    assert instance == True
