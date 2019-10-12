import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import pytest
import sys

sys.path.append("..")
import database

@pytest.fixture(autouse=True, scope="session")
def run_around_tests():
    sys.path.append("..")
    cred = credentials.Certificate("firestore_creds.json")
    firebase_admin.initialize_app(
        cred, {
            "databaseURL": "https://ghs-app-5a0ba.firebaseio.com/",
            'databaseAuthVariableOverride': {
                'uid': 'my-service-worker'
            }
        })
    assert True == True

def test_set_monitoring_info():
    """Tests for the send email function
    """
    diff_time = 4
    result = database.set_monitoring_info(True, diff_time)
    ref = db.reference("db-info/monitoring/Server-Monitor")
    ref_data = ref.get()
    assert ref_data == result

def test_update_pulse():
    """
    Test for the update_pulse function
    """
    service_name = "Server-Monitor-CI"
    instance = database.update_pulse(1, service_name)
    ref = db.reference("db-info/pulses/" + service_name)
    ref_data = ref.get()
    ref.set({})
    assert instance == ref_data
