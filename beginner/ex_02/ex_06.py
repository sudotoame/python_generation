x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

a1 = x1 + y1
b1 = x2 + y2
a2 = x1 - y1
b2 = x2 - y2
if a1 == b1 or a2 == b2:
    print("YES")
else:
    print("NO")
