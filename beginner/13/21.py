num = int(input())

for i in range(1, num + 1):
    if (i >= 5 and i <= 9) or ( i >= 17 and i <= 37) or (i >= 78 and i <= 87):
        continue
    print(i)