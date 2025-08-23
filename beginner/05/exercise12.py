# 1, 3, 5, 7, 8, 10, 12 месяцы - 31 день
# 4, 6, 9, 11 - 30
# 2 - 28

a = int(input())

if a == 2:
    print("28")
elif a == 4 or a == 6 or a == 9 or a == 11:
    print("30")
else:
    print("31")
