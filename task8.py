POUNDS_TO_KILOGRAMS = 0.45359237


print("Фунты\tКилограммы")
print("------\t----------")


for pounds in range(1, 11):
    kilograms = pounds * POUNDS_TO_KILOGRAMS

    print(f"{pounds}\t{kilograms:.2f}")
