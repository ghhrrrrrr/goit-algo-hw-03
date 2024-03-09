import datetime
import re
import random

def get_days_from_today(date):
    right_pattern = re.findall('^\d{4}-\d{2}-\d{2}$', date)
    if len(right_pattern) < 1:
        raise ValueError
    date_today = datetime.datetime.today()
    items = date.split("-")
    specific_date = datetime.datetime(int(items[0]),int(items[1]),int(items[2]))
    difference = date_today.toordinal() - specific_date.toordinal()
    return difference

def get_numbers_ticket(min, max, quantity):
    if not min >= 1 and max <= 1000 and 1 <= quantity <= 1000:
        raise ValueError
    result = set()
    while len(result) < quantity:
        result.add(random.randint(min, max))
    
    return sorted(result)

def normalize_phone(phone_number):
    new_phone = (
        phone_number.strip()
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    if new_phone.find("+38", 0, 3) >= 0:
        return new_phone
    elif new_phone.find("38", 0, 2) >= 0:
        new_phone = '+' + new_phone
    else:
        new_phone = '+38' + new_phone

    return new_phone
