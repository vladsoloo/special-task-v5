exchange_rate = float(input("Введите текущий курс доллара к рублю: "))


print("Доллары\tРубли")
print("-------\t-------")


for dollars in range(1, 21):
    rubles = dollars * exchange_rate

    print(f"{dollars}\t{rubles:.2f}")
