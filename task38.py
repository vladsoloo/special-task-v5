def calculate_position_and_distance(n):
    position = 0
    total_distance = 0

    for i in range(1, n + 1):
        distance = 1 / i
        total_distance += distance




        if i % 2 == 1:
            position += distance
        else:
            position -= distance

    return position, total_distance


n = 100
position, total_distance = calculate_position_and_distance(n)

print(f"После {n}-го этапа мужчина будет находиться на расстоянии {position:.6f} 
      км от дома.")
print(f"Общий путь, пройденный мужчиной: {total_distance:.6f} км.")
