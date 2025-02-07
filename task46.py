resistances = [10, 20, 30]


inverse_sum = sum(1 / r for r in resistances)


total_resistance = 1 / inverse_sum

print(f"Общее сопротивление цепи: {total_resistance:.2f} Ом")
