def sum_fractions():
    total_sum = 0

    for num in range(2, 11):
        denom = num + 1
        total_sum += num / denom

    return total_sum


result = sum_fractions()
print(f"Сумма дробей: {result:.2f}")
