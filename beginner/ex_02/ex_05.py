num = int(input())

if (num % 2 == 0) and (num >= 2 and num <= 5):
    print("NO")
elif (num % 2 == 0) and (num >= 6 and num <= 20):
    print("YES")
elif (num % 2 == 0) and (num > 20):
    print("NO")
elif num % 2 != 0:
    print("YES")
