import math


p0 = 1.29
z = 25000


def density_at_height(h):
    return p0 * math.exp(-h / z)


print("Высота (м)\tПлотность (кг/м^3)")
print("----------------------")


for height in range(0, 1100, 100):
    rho = density_at_height(height)
    print(f"{height}\t{rho:.4f}")
