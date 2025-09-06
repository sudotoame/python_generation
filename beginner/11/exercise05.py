m, n = int(input()), int(input())

for i in range(m, n + 1, -1):
    if not i % 2 == 0:
        print(i)
