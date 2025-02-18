def multiply_recursive(x, y):
    if y == 0:
        return 0
    return x + multiply_recursive(x, y - 1)


x, y = 6, 4
print(multiply_recursive(x, y))
