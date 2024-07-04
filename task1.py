from datetime import datetime

def get_days_from_today(date):
    # Парсимо вхідну дату у форматі 'РРРР-ММ-ДД'
    input_date = datetime.strptime(date, '%Y-%m-%d').date()
    
    # Отримуємо поточну дату
    current_date = datetime.now().date()
    
    # Рахуємо різницю у днях
    delta_days = (current_date - input_date).days
    
    return delta_days

# Приклад використання:
date_string = '2020-10-09'
days_difference = get_days_from_today(date_string)
print(f"Days difference from {date_string} to today: {days_difference}")