num = int(input())
last_digit = 0

while num != 0:
    last_digit = num % 10
    print(last_digit, end="")
    num = num // 10
