INCHES_TO_CM = 2.54


print("Дюймы\tСантиметры")
print("-----\t---------")


for inches in range(10, 23):
    cm = inches * INCHES_TO_CM

    print(f"{inches}\t{cm:.2f}")
