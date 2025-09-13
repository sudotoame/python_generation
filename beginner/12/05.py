from math import log

n = int(input())
res = 0
for i in range(1, n):
    res = res + (1 / (i + 1))

print(res + 1 - log(n))
