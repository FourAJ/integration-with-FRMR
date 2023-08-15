from datetime import datetime


def getTime(strDate: str) -> datetime or None:
    date_parts, time_parts = strDate.split('T')
    year, month, day = map(int, date_parts.split('-'))
    hours, minutes, seconds = map(int, time_parts.split('.')[0].split(':'))
    if year > 9999 or month > 12 or day > 31 or hours > 23 or minutes > 59 or seconds > 59:
        return None
    return strDate
