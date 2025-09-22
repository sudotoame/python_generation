num = int(input())

count = 0

for i in range(num):
    for j in range(i + 1):
        count += 1
        print(count, end="")
    for k in range(i, 0, -1):
        count -= 1
        print(count, end="")
    count = 0
    print()
