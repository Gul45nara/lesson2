def is_year_leap(year):
    """Определяет, является ли год високосным"""
    return year % 4 == 0

# Пример использования функции
test_year = 2024  
result = is_year_leap(test_year)

# Вывод результата
print(f"год {test_year}: {result}")