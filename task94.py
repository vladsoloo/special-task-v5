import math


def task_5_94(num):
    """
    Находит сумму цифр шестизначного числа
    """
    if not 100000 <= num <= 999999:
        return "Число должно быть шестизначным"

    return sum(int(digit) for digit in str(num))


print("Задача 5.94 (123456):", task_5_94(123456))
