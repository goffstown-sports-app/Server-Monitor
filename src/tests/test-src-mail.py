import unittest
import sys
import codecs

sys.path.append("..")
import mail


class TestMail(unittest.TestCase):
    """Runs tests for /src/mail.py
    """

    def test_send_email(self):
        """Tests for the send email function
        """
        html_file = codecs.open("test.html", "r")
        instance = mail.send_email(html_file.read(), "ghsappbot@gmail.com", "CI TEST")
        html_file.close()
        self.assertEqual(instance, True)
        


if __name__ == "__main__":
    unittest.main()
