num = int(input())

last_digit = num % 10
count_last_digit = 0
count_for_three = 0
count_for_even = 0
sum_largest_five = 0
mul_largest_seven = 1
count_for_zero_five = 0
count_for_mul = 0
digit_for_mul = 0
while num > 0:
    local_last_digit = num % 10
    if local_last_digit == 3:
        count_for_three += 1
    if last_digit == local_last_digit:
        count_last_digit += 1
    if local_last_digit % 2 == 0:
        count_for_even += 1
    if local_last_digit > 5:
        sum_largest_five += local_last_digit
    if local_last_digit > 7:
        mul_largest_seven *= local_last_digit
        count_for_mul += 1
        digit_for_mul = local_last_digit
    if local_last_digit == 0 or local_last_digit == 5:
        count_for_zero_five += 1
    num //= 10

print(count_for_three)
print(count_last_digit)
print(count_for_even)
print(sum_largest_five)
if count_for_mul == 1:
    print(digit_for_mul)
elif count_for_mul == 0:
    print("1")
else:
    print(mul_largest_seven)
print(count_for_zero_five)
