num1 = int(input())

num = (num1 // 2) + 1

for i in range(num):
    for j in range(i + 1):
        print("*", end="")
    print()

for i in range(num, 1, -1):
    for j in range(i - 1):
        print("*", end="")
    print("")
