from math import pi
v = 0
r = 10
for _ in range(12):
    v = v+(4/3) * pi * r**3
    r += 0.5
print(v)
