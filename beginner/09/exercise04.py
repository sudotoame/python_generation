import math

s = float(input())

r = (s * math.pi) / 180

res = math.sin(r) + math.cos(r) + math.tan(r) ** 2

print(res)
