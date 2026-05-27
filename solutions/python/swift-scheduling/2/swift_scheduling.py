'''Functions for the Booking Up For Beauty exercise.'''
from datetime import datetime, timedelta

def delivery_date(start, description):
    '''Convert a delivery date description to an ISO datetime string.

    Args:
        start: ISO datetime string of the meeting start.
        description: Fixed ("NOW", "ASAP", "EOW") or variable ("<N>M", "Q<N>") code.

    Returns:
        ISO datetime string of the delivery date.'''
    
    meeting = datetime.fromisoformat(start)

    if description == 'NOW':
        return (meeting + timedelta(hours=2)).isoformat()

    if description == 'ASAP':
        days, hour = (0, 17) if meeting.hour < 13 else (1, 13)
        return (meeting + timedelta(days=days)).replace(hour=hour, minute=0, second=0).isoformat()

    if description == 'EOW':
        wday = meeting.weekday()
        extra_days, hour = (4 - wday, 17) if wday < 3 else (6 - wday, 20)
        return (meeting + timedelta(days=extra_days)).replace(hour=hour, minute=0, second=0).isoformat()

    if description[-1] == 'M':
        dmonth = int(description[:-1])
        extra_year = 1 if meeting.month >= dmonth else 0
        dmeeting = meeting.replace(
            year=meeting.year + extra_year,
            month=dmonth, day=1,
            hour=8, minute=0, second=0)
        while dmeeting.weekday() >= 5:
            dmeeting += timedelta(days=1)
        return dmeeting.isoformat()

    if description[0] == 'Q':
        dquarter = int(description[1])
        extra_year = 1 if (meeting.month + 2) // 3 > dquarter else 0
        dmonth = dquarter * 3
        dmeeting = meeting.replace(
            year=meeting.year + extra_year,
            month=dmonth, day=1,
            hour=8, minute=0, second=0)
        if dmonth == 12:
            next_first = dmeeting.replace(year=dmeeting.year + 1, month=1, day=1)
        else:
            next_first = dmeeting.replace(month=dmonth + 1, day=1)
        dmeeting = next_first - timedelta(days=1)
        while dmeeting.weekday() >= 5:
            dmeeting -= timedelta(days=1)
        return dmeeting.isoformat()
    raise ValueError('Unknown description')