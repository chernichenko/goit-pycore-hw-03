import random

def get_numbers_ticket(min_val, max_val, quantity):
    # Перевіряємо, чи відповідають параметри вказаним обмеженням
    if min_val < 1 or max_val > 1000 or min_val > max_val or quantity < 1 or quantity > (max_val - min_val + 1):
        return []
    
    # Генеруємо унікальні випадкові числа
    numbers = random.sample(range(min_val, max_val + 1), quantity)
    
    # Сортуємо числа перед поверненням
    numbers.sort()
    
    return numbers

# Приклад використання:
min_val = 1
max_val = 49
quantity = 6
result = get_numbers_ticket(min_val, max_val, quantity)
print(f"Generated numbers: {result}")
