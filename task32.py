n = int(input("вставьте число от 1 до 10 "))
s = 1
j = 1
for i in range(1, n + 1):
    j *= i
    print(j)
    s += 1 / j
print('Sum: ', s)
