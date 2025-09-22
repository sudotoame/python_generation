num = int(input())

last_digit = num % 10
flag = True

while num != 0:
    reversed_num = num % 10
    if last_digit > reversed_num:
        flag = False
    last_digit = reversed_num
    num //= 10

if flag is True:
    print("YES")
else:
    print("NO")
