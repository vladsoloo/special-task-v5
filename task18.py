def calculate_y(t):
    return 3.5 * t ** 2 - 7 * t + 16


xs = range(2, 17)


for x in xs:
    t = x + 2
    y = calculate_y(t)
    print(f'При x = {x}, y = {y:.2f}')
