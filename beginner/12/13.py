flag = True
for _ in range(10):
    n = int(input())
    if not (n % 2) == 0:
        flag = False
        break
    else:
        flag = True

if flag is True:
    print("YES")
else:
    print("NO")
