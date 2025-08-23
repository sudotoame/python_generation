a, b, c = int(input()), int(input()), int(input())

if b > a and b < c or b < a and b > c:
    print(b)
elif a > b and a < c or a < b and a > c:
    print(a)
elif c > b and c < a or c < b and c > a:
    print(c)
