import math

def square(side):
    """Вычисляет площадь квадрата, округляя вверх для нецелых сторон"""
    area = side ** 2
    return math.ceil(area) if not isinstance(side, int) else area

# Примеры использования
print(square(5))     # 25 (целое число)
print(square(3.2))   # 11 (3.2² = 10.24 → округляем до 11)
print(square(4.0))   # 16 (4.0 считается как int)