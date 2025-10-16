from datetime import datetime, date, timedelta

def get_upcoming_birthdays(users):
    """
    Повертає список словників з полями:
      - name: ім'я користувача
      - congratulation_date: YYYY.MM.DD (дата привітання)
    Враховує вікно у 7 днів від today (включно), переносить вихідні на понеділок.
    Параметр today залишено для зручного тестування; за замовчуванням береться поточна дата.
    """

    today = datetime.today().date()
    end = today + timedelta(days=7)
    result = []

    for user in users:
        # 1) Парсимо дату народження
        bday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # 2) Дата дня народження у поточному році (з обробкою 29 лютого)
        try:
            bday_this_year = bday.replace(year=today.year)
        except ValueError:
            # якщо 29 лютого у невисокосний рік — вітаємо 28 лютого
            bday_this_year = date(today.year, 2, 28)

        # 3) Якщо вже минуло — беремо наступний рік
        if bday_this_year < today:
            try:
                next_bday = bday.replace(year=today.year + 1)
            except ValueError:
                next_bday = date(today.year + 1, 2, 28)
        else:
            next_bday = bday_this_year

        # 4) Перевіряємо, що ДН у вікні [today; today+7]
        if today <= next_bday <= end:
            congr_date = next_bday

            # 5) Якщо вихідний — переносимо на понеділок
            if congr_date.weekday() >= 5:  # 5=Субота, 6=Неділя
                days_to_next_monday = 7 - congr_date.weekday()
                congr_date = congr_date + timedelta(days=days_to_next_monday)

            result.append({
                "name": user["name"],
                "congratulation_date": congr_date.strftime("%Y.%m.%d"),
            })

    # 6) Відсортуємо за датою привітання (і ім'ям для стабільності)
    result.sort(key=lambda x: (x["congratulation_date"], x["name"]))
    return result

users = [
    {"name": "John Doe",  "birthday": "2024.02.29"},
    {"name": "Jane Smith","birthday": "1989.10.18"},
]

upcoming = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:\n", upcoming)
