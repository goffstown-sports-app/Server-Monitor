from datetime import datetime


def cast_regular_as_datetime(regular_time):
    """Convert regular time format to datetime object
    
    Arguments:
        regular_time {string} -- regular time format
    
    Returns:
        datetime.datetime -- datetime object for regular time
    """
    date_section = regular_time.split(" ")[0].split("-")
    year = int(date_section[0])
    month = int(date_section[1])
    day = int(date_section[2])
    day_section = regular_time.split(" ")[1].split(":")
    hour = int(day_section[0])
    minute = int(day_section[1])
    second = int(date_section[2])
    datetime_object = datetime(year, month, day, hour, minute, second)
    return datetime_object
