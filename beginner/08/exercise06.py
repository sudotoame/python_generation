a, b, c = input(), input(), input()

length_1 = len(a)
length_2 = len(b)
length_3 = len(c)

maximum = max(length_1, length_2, length_3)
minimum = min(length_1, length_2, length_3)
middle = 0
if length_1 != maximum and length_1 != minimum:
    middle = length_1
elif length_2 != maximum and length_2 != minimum:
    middle = length_2
else:
    middle = length_3

print(maximum, minimum, middle)

if maximum - middle == middle - minimum:
    print("YES")
else:
    print("NO")

