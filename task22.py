price = float(input("Введите цену за килограмм: "))

for i in range(1, 21):
    weight = i * 100
    cost = price * weight / 1000
    print(f"{weight} грамм = {cost:.2f} у.е.")
