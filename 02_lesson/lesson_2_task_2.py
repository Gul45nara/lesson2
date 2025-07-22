def is_year_leap(year):
    """Определяет високосный год"""
    return year % 4 == 0


# Проверка
test_year = 2024
print(f"год {test_year}: {is_year_leap(test_year)}")
