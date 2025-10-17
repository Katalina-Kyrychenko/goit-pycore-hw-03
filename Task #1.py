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
        # Якщо формат дати неправильний — повідомлення користувачу
        print("Помилка: неправильний формат дати. Використовуйте 'YYYY-MM-DD'.")
        return None
    
print(f'Різницю у днях становить: {get_days_from_today("2021-10-09")} днів.')