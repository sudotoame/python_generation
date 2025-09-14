num = int(input())

a = 1
b = 5
c = 10
d = 25

counter = 0

while num != 0:
    if num >= 25:
        counter += 1
        num -= d
    elif num >= 10:
        counter += 1
        num -= c
    elif num >= 5:
        counter += 1
        num -= b
    elif num >= 1:
        counter += 1
        num -= a

print(counter)
