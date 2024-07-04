from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_until_birthday = (birthday_this_year - today).days

        if 0 <= days_until_birthday <= 7:
            congratulation_date = birthday_this_year

            # Переносимо на наступний робочий день, якщо потрібно
            if congratulation_date.weekday() >= 5:  # якщо субота або неділя
                congratulation_date += timedelta(days=7 - congratulation_date.weekday())

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

# Приклад використання:
users = [
    {"name": "John", "birthday": "2000.07.04"},
    {"name": "Alice", "birthday": "1995.07.06"},
    {"name": "Bob", "birthday": "1990.07.10"},
    {"name": "Eve", "birthday": "1985.07.15"},
    {"name": "Charlie", "birthday": "1980.07.20"},
    {"name": "Mia", "birthday": "1992.07.24"},
]

upcoming = get_upcoming_birthdays(users)
for birthday in upcoming:
    print(f"{birthday['name']} - {birthday['congratulation_date']}")
