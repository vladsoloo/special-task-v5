def class_average(grades):
    return sum(grades) / len(grades)


students = [86, 78, 89, 76, 91, 83, 79, 82, 87, 75]
print("Средняя оценка по физике для класса:", class_average(students))
