import math

n, a = int(input()), float(input())

res = (n * (a**2)) / (math.tan((math.pi / n)) * 4)

print(res)
