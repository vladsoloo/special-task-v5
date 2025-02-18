def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


def series_sum(n):
    total = 1
    for i in range(1, n + 1):
        total += 1/factorial(i)
    return total


n = int(input("Введите число n (1 < n ≤ 10): "))
print(series_sum(n))
