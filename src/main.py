import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
import datetime
from time import sleep
from os import system

import database
import mail


def main():
    """Runs the main program
    """
    cred = credentials.Certificate("firestore_creds.json")
    firebase_admin.initialize_app(
        cred, {
            "databaseURL": "https://ghs-app-5a0ba.firebaseio.com/",
            'databaseAuthVariableOverride': {
                'uid': 'my-service-worker'
            }
        })
    


if __name__ == "__main__":
    main()
