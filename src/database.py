from firebase_admin import db


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