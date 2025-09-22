num = int(input())
b = ""
while num > 0:
    remainder = str(num % 2) + b
    print(remainder, end="")
    num //= 2
