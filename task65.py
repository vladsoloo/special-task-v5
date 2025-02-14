population = [50, 70, 90, 110, 130, 150, 120, 140, 160, 180, 190, 210]


density = [2, 2.5, 3, 3.5, 4, 4.5, 3.75, 4.25, 4.75, 5, 5.25, 5.5]


areas = [pop / den for pop, den in zip(population, density)]


total_area = sum(areas)


print(f"Общая площадь территории области: {total_area:.2f} км²")
