num = int(input())

for i in range(1, num + 1):
    if i == 1:
        print("*" * 19)
    elif i == num:
        print("*" * 19)
    else:
        print("*", " " * 15, "*")
