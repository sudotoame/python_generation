n = "asdsa"

last = len(n) - 1
first = 0
flag = True

while first < last:
    if n[first] != n[last]:
        flag = False
        break
    first += 1
    last -= 1

if flag:
    print("Палиндром")
else:
    print("Не палиндром")
