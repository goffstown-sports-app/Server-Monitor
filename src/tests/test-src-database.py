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
        diff_time = 4
        result = database.set_monitoring_info(True, diff_time)
        ref = db.reference("db-info/monitoring/Server-Monitor")
        self.assertEqual(ref.get(), result)

    def test_update_pulse(self):
        """
        Test for the update_pulse function
        """
        instance = database.update_pulse(1, service_name)
        ref = db.reference("db-info/pulses/" + service_name)
        ref_data = ref.get()
        self.assertEqual(instance, ref_data)


if __name__ == "__main__":
    service_name = "Server-Monitor-CI"
    cred = credentials.Certificate("firestore_creds.json")
    firebase_admin.initialize_app(
        cred, {
            "databaseURL": "https://ghs-app-5a0ba.firebaseio.com/",
            'databaseAuthVariableOverride': {
                'uid': 'my-service-worker'
            }
        })
    unittest.main()
