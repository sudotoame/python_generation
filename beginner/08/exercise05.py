a, b, c = input(), input(), input()

length_1 = len(a)
length_2 = len(b)
length_3 = len(c)

if length_1 < length_2 and length_1 < length_3:
    print(a)
elif length_2 < length_1 and length_2 < length_3:
    print(b)
elif length_3 < length_1 and length_3 < length_2:
    print(c)

if length_1 > length_2 and length_1 > length_3:
    print(a)
elif length_2 > length_1 and length_2 > length_3:
    print(b)
elif length_3 > length_1 and length_3 > length_2:
    print(c)
