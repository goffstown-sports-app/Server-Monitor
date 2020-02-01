from firebase_admin import db
from datetime import datetime
import platform
import os


def set_service_status(service_name, status, last_time_online, last_time_offline):
    """Set a true or false status for each service
    
    Arguments:
        service_name {string} -- name of the service
        status {boolean} -- offline or not
        last_time_online {string} -- time when application was last online
        last_time_offline {string} -- time when application was last offline
    
    Returns:
        dict -- what the application was set as
    """
    ref = db.reference("db-info/statuses/" + service_name)
    ref_set = {
            "online": status,
            "last-time-online": last_time_online,
            "last-time-offline": last_time_offline
        }
    ref.set(ref_set)
    return ref_set
