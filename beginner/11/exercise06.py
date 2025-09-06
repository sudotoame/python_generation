m, n = int(input()), int(input())

if m == n:
    print(m)
else:
    for i in range(m, n + 1):
        if (m == n) or (i % 17 == 0) or (i % 10 == 9) or (i % 3 == 0 and i % 5 == 0):
            print(i)
