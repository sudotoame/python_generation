num = int(input())
has_seven = False

while num != 0:
    last_digit = num % 10
    if last_digit == 7:
        has_seven = True
    num /= 10

if has_seven is True:
    print("YES")
else:
    print("NO")
