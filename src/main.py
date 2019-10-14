import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
import datetime
from time import sleep
import codecs
from ghsTools import ghsTools

import database
import mail
from utils import datetime_utils
from utils.generic import clear_output


def main():
    """Runs the main program
    """
    cred = credentials.Certificate("./secrets/firestore_creds.json")
    firebase_admin.initialize_app(
        cred, {
            "databaseURL": "https://ghs-app-5a0ba.firebaseio.com/",
            'databaseAuthVariableOverride': {
                'uid': 'my-service-worker'
            }
        })
    recent_problems = []
    pulse_amount = 0
    last_time_offline = {}
    last_time_online = {}
    ghsTools().set_monitoring_info(True, time_till_next_run, "Server-Monitor")
    while True:
        time_till_next_run = 7
        pulse_amount += 1
        db_info_ref = db.reference("db-info").get()
        monitoring_info = db_info_ref["monitoring"]
        with open("email_list.txt") as email_list_file:
            email_list = email_list_file.read().split("\n")
        for service_name in monitoring_info:
            clear_output(5)
            print("--------------------------------")
            print("Checking:", service_name)
            service_info = monitoring_info[service_name]
            print("Service Information:", service_info)
            service_pulse_time = db_info_ref["pulses"][service_name]["Pulse-Time"]
            current_time = datetime.datetime.now()
            datetime_version_of_pulse_time = datetime_utils.cast_regular_as_datetime(
                service_pulse_time)
            time_diff = current_time - datetime_version_of_pulse_time
            seconds_diff = time_diff.seconds
            print("Time Diff for Service:", seconds_diff)
            if service_info["email-notification"]:
                if seconds_diff > service_info["pulse-time-diffs-(secs)"] and service_name not in recent_problems:
                    print("Problem with", service_name, "sending email now")
                    with codecs.open("problem.html", "r") as problem_html:
                        problem_html_lines = problem_html.read()
                    filled_html_file = problem_html_lines.format(
                        program_name=service_name, pulse_rate=service_info["pulse-time-diffs-(secs)"], pulse_time_delta=service_info["pulse-time-diffs-(secs)"])
                    for email in email_list:
                        mail.send_email(
                            filled_html_file, email, "Problem with " + service_name)
                    recent_problems.append(service_name)
                elif service_name in recent_problems and seconds_diff < service_info["pulse-time-diffs-(secs)"]:
                    print(service_name, "is back online, sending email")
                    with codecs.open("good_status.html", "r") as good_status_html:
                        good_status_lines = good_status_html.read()
                    filled_html_file = good_status_lines.format(
                        program_name=service_name, pulse_rate=service_info["pulse-time-diffs-(secs)"])
                    for email in email_list:
                        mail.send_email(filled_html_file,
                                        email, service_name + " Fixed")
                    recent_problems.remove(service_name)
                else:
                    print(service_name, "looks fine")
            try:
                if pulse_amount == 1:
                    last_time_offline[service_name] = db_info_ref["statuses"][service_name]["last-time-offline"]
                    last_time_online[service_name] = db_info_ref["statuses"][service_name]["last-time-online"]
            except KeyError:
                last_time_offline[service_name] = "N/A"
                last_time_online[service_name] = "N/A"
            if seconds_diff > service_info["pulse-time-diffs-(secs)"]:
                last_time_offline[service_name] = str(datetime.datetime.now())
                database.set_service_status(
                    service_name, False, last_time_online[service_name], last_time_offline[service_name])
            else:
                last_time_online[service_name] = str(datetime.datetime.now())
                database.set_service_status(
                    service_name, True, last_time_online[service_name], last_time_offline[service_name])
        ghsTools().update_pulse(pulse_amount, "Server-Monitor")
        sleep(time_till_next_run)


if __name__ == "__main__":
    main()
