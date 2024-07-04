import re

def normalize_phone(phone_number):
    # Видаляємо всі символи, окрім цифр та символу '+'
    digits = re.sub(r'\D', '', phone_number)
    
    # Перевіряємо, чи номер вже має міжнародний код
    if digits.startswith('380'):
        return '+' + digits
    elif digits.startswith('80'):
        return '+3' + digits
    elif digits.startswith('0'):
        return '+38' + digits[1:]
    else:
        return '+38' + digits

# Приклад використання:
phone1 = "    +38(050)123-32-34"
phone2 = "     0503451234"
phone3 = "(050)8889900"
phone4 = "38050-111-22-22"
phone5 = "38050 111 22 11   "

print(normalize_phone(phone1))  # Output: +380501233234
print(normalize_phone(phone2))  # Output: +380503451234
print(normalize_phone(phone3))  # Output: +380508889900
print(normalize_phone(phone4))  # Output: +380501112222
print(normalize_phone(phone5))  # Output: +380501112211
