num = int(input())
sum = 0
mul = 1
count = 0
last_digit = 0
digit = 0

while num != 0:
    last_digit = num % 10
    count += 1
    if count == 1:
        digit = last_digit
    sum += last_digit
    mul *= last_digit

    num //= 10

print(sum)
print(count)
print(mul)
print(sum / count)
print(last_digit)
print(last_digit + digit)
