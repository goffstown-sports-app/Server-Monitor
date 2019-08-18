import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import unittest
import sys

sys.path.append("..")
import database


class TestDatabase(unittest.TestCase):
    """Runs tests for /src/database.py
    """

    def test_set_monitoring_info(self):
        """Tests for the send email function
        """
        cred = credentials.Certificate("firestore_creds.json")
        firebase_admin.initialize_app(
            cred, {
                "databaseURL": "https://ghs-app-5a0ba.firebaseio.com/",
                'databaseAuthVariableOverride': {
                    'uid': 'my-service-worker'
            }
        })
        diff_time = 10
        result = database.set_monitoring_info(True, diff_time)
        ref = db.reference("db-info/monitoring/Server-Monitor")
        self.assertEqual(ref.get(), result)


if __name__ == "__main__":
    unittest.main()
