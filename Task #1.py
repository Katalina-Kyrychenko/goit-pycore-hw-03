from datetime import datetime

def get_days_from_today(date_str):
    try:
        # 1 Перетворюємо вхідний рядок у об’єкт datetime.date
        input_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        
        # 2 Отримуємо поточну дату
        today = datetime.today().date()
        
        # 3 Обчислюємо різницю у днях (today - input_date)
        delta = today - input_date
        
        # 4 Повертаємо різницю у днях (може бути від’ємною)
        return delta.days

    except ValueError:
        # 5 Обробка некоректного формату
        print(f"Помилка: '{date_str}' — неправильний формат дати. Використовуйте формат 'YYYY-MM-DD'.")
        return None

def print_days_difference(days_difference):
    if days_difference is not None:
        print(f'Різниця у днях становить: {days_difference} днів.')

print_days_difference(get_days_from_today("2021-10-09"));
print_days_difference(get_days_from_today("13.14.2000"));
print_days_difference(get_days_from_today("2025/05/01"));