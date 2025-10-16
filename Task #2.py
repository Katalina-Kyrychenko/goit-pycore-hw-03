import random

def get_numbers_ticket(min, max, count):
    # Перевірка коректності вхідних параметрів
    if not (min < max and count > 0):
        return []
    # Генерація унікальних випадкових чисел
    numbers = random.sample(range(min, max + 1), count)
    #sorted_numbers = numbers.sort();
    numbers.sort()
    print("Відсортована послідовність:", numbers);
    # Повертаємо відсортований список
    #return sorted(numbers)
    return numbers


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
