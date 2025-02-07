lis = [x for x in range(50, 1000 + 1, 50)]
cost = float(input('Стоимость 1000 г сыра (в рублях): '))
print('Стоимость:')
for x in lis:
    print(f'{x} граммов - {cost*x/1000} руб')
