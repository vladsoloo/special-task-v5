def main():

    print("Введите десять чисел:")
    numbers = []
    
    for i in range(1, 11):
        number = float(input(f"Введите {i}-е число: "))
        numbers.append(number)
        

    sum_of_squares = sum([num ** 2 for num in numbers])
    

    print(f"Сумма квадратов введенных чисел равна {sum_of_squares}")

if __name__ == "__main__":
    main()
