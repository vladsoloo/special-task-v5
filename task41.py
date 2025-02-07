n = int(input("Введите натуральное число n: "))


numbers = []
for i in range(n):
    num = float(input(f"Введите вещественное число a{i+1}: "))
    numbers.append(num)


total_sum = sum(numbers)


print("Сумма всех вещественных чисел:", total_sum)
