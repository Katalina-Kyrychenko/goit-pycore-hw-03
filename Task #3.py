import re

def normalize_phone(phone_number):
    # 1 Прибираємо зайві пробіли на початку та в кінці
    phone_number = phone_number.strip()

    # 2 Видаляємо всі символи, крім цифр і '+'
    cleaned_number = re.sub(r'[^\d+]', '', phone_number)

    # 3 Логіка визначення міжнародного коду
    if cleaned_number.startswith('+'):
        # Якщо вже є '+', просто повертаємо очищений номер
        return cleaned_number
    elif cleaned_number.startswith('380'):
        # Якщо починається з '380' без '+', додаємо '+'
        return '+' + cleaned_number
    else:
        # Якщо немає коду країни — додаємо '+38' перед номером
        return '+38' + cleaned_number


# Приклад використання
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)