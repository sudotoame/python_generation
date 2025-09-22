num = int(input())


flag = False
pre_last = 0
last_digit = num % 10


while num != 0:
    pre_last = num % 10
    if last_digit != pre_last:
        flag = True
    num = num // 10


if flag is True:
    print("NO")
else:
    print("YES")
