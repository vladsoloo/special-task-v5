import math


def task_5_92(n=50):
    """
    Вычисляет сумму √1 + √2 + √3 + ... + √50
    """
    return sum(math.sqrt(i) for i in range(1, n + 1))


print("Задача 5.92:", task_5_92())
