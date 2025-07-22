def fizz_buzz(n):
    """
    Печатает числа от 1 до n с заменой по правилам:
    - Fizz для чисел, кратных 3
    - Buzz для чисел, кратных 5
    - FizzBuzz для чисел, кратных 15
    """
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


# Пример использования
fizz_buzz(20)
