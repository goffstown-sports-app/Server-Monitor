from firebase_admin import db
import datetime
import platform
import os


def set_monitoring_info(email_notifications, pulse_time_diff_secs):
    """Updates the monitoring section for this micro service

    Arguments:
        email_notifications {bool} -- if the user should get email notifications
        pulse_time_diff_secs {int} -- amount of seconds between each pulse (exact)

    Returns:
        dict -- what the monitoring info was set as
    """
    ref = db.reference("db-info/monitoring/Server-Monitor")
    ref_set = {
        "email-notification": email_notifications,
        "pulse-time-diffs-(secs)": pulse_time_diff_secs + 120,
        "pulse-time-diffs-exact-(secs)": pulse_time_diff_secs
    }
    ref.set(ref_set)
    return ref_set


def update_pulse(consecutive_number_of_runs, service_name):
    """Updates the pulse for this application
    Arguments:
        consecutive_number_of_runs {int} -- how many times the application has ran in a row
        service_name {str} -- name of the service
    Returns:
        dict -- what the pulse was set as in the database
    """
    current_time = str(datetime.now())
    ref = db.reference("db-info/pulses/" + service_name)
    if "linux" in str(platform.platform()).lower():
        ip_command = str(os.popen("hostname -I").read())
        ip = ip_command.split(" ")[0]
    else:
        ip = ""
    ref_set = {
        "Pulse-Time": current_time,
        "Pulse-Amount-(Consecutive)": consecutive_number_of_runs,
        "Pulse-Node": str(platform.uname().node),
        "Pulse-OS": str(platform.platform()),
        "Pulse-Python-Version": str(platform.python_version()),
        "Pulse-IP": ip
    }
    ref.set(ref_set)
    return ref_set
