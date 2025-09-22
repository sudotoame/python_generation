mx = None
s = 0
for i in range(1, 11): # без стартового аргумента, тут будет 11 итераций с 0 до 10
    x = int(input())
    if x < 0:
        s += x # просто присваивая числа, мы не получим сумму отрицательных чисел
        if mx is None or x > mx:
            mx = x
if mx is None:
    print("NO")
else:
    print(s)
    print(mx)