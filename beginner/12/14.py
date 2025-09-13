n = int(input())

f1 = 0
f2 = 1

for i in range(0, n):
    f1, f2 = f2, f1 + f2
    print(f1, end=" ")
