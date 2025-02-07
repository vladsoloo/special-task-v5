def calculate_y(t):
    return 2 * t**2 + 5.5 * t - 2


xs = range(4, 29)


for x in xs:
    t = x + 2
    y = calculate_y(t)
    print(f'При x = {x}, y = {y:.2f}')
