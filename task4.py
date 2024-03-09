from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        while birthday_this_year.weekday() >= 5:
            birthday_this_year += timedelta(days=1)

        upcoming_birthdays.append({
            "name": user["name"],
            "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
        })

    return upcoming_birthdays