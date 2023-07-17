from datetime import datetime, date

def validate_date(date_string: str):
    try:
        # Try to convert the string to a date object
        dt = datetime.strptime(date_string, '%Y-%m-%d').date()
        # Check if the date is not in the past
        if dt < date.today():
            return False
        # Date is valid and not in the past
        return True
    except ValueError:
        # Date is not in the expected format
        return False