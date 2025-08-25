year = int(input())

last_digit = year % 10
prelast_gigit = (year % 100) // 10

if last_digit == 0 and prelast_gigit == 0:
    print("YES")
else:
    print("NO")
