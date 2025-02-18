def compute_expression():
    result = 20**2
    for i in range(19, 0, -1):
        result = (result - i**2)**2
    return result


print(compute_expression())
