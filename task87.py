def square_sum():
    total = 0
    for n in range(1, 11):
        square = 0
        for i in range(n):
            square += 2*i + 1
        total += square
    return total


print(square_sum())
