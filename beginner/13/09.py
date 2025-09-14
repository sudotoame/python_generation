num = int(input())
count = 0

while num >= -1 and num < 6:
    if num == 5:
        count += 1
    num = int(input())
print(count)
