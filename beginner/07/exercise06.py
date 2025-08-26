a1, a2, b1, b2 = int(input()), int(input()), int(input()), int(input())

res = (abs(a1) - abs(a2)) + (abs(b1) - abs(b2))
ares = a1 - b1
bres = a2 - b2

ress = abs(ares) + abs(bres)

print(ress)
