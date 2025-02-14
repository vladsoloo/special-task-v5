class1_heights = [170, 165, 175, 180, 168, 172, 169, 173, 176, 178]


class2_heights = [171, 166, 174, 181, 167, 173, 170, 172, 177, 179]


def calculate_average_height(heights):
    return sum(heights) / len(heights)


avg_class1 = calculate_average_height(class1_heights)
print(f"Средний рост учеников первого класса: {avg_class1:.2f} см")


avg_class2 = calculate_average_height(class2_heights)
print(f"Средний рост учеников второго класса: {avg_class2:.2f} см")
