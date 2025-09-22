counter = 0
for i in range(99, 102): # 102 - 1
    temp = i # 99 -> 100 -> 101
    while temp > 0:
        counter += 1 # 2+3+3 = 8
        temp //= 10

print(counter)