import math


def task_5_96():
    """
    Решение задачи о наклонной палке
    """
    L = 4.5
    h = 3.0
    step = 0.2

    results = []
    current_h = h

    while current_h > 0:

        angle = math.degrees(math.acos(current_h / L))
        results.append((current_h, angle))
        current_h -= step

    return results


print("Задача 5.96 (первые 5 значений):", task_5_96()[:5])
