x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

res_1 = (x1 + y1) % 2
res_2 = (x2 + y2) % 2

if res_1 == res_2:
    print("YES")
else:
    print("NO")
