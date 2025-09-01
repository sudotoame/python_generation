import math

a, b = float(input()), float(input())

r1 = (a + b) / 2
r2 = math.sqrt(a * b)
r3 = ((a * b) * 2) / (a + b)
r4 = math.sqrt(((a**2) + (b**2)) / 2)

print(r1)
print(r2)
print(r3)
print(r4)
