def total_scores(first_student, second_student):
    first_total = sum(first_student)
    second_total = sum(second_student)
    print("Сумма оценок первого ученика:", first_total)
    print("Сумма оценок второго ученика:", second_total)

first_student = [8, 9, 10, 7, 8]
second_student = [9, 8, 9, 8, 9]
total_scores(first_student, second_student)
