n = int(input())

maximum1 = 0
maximum2 = 0

for i in range(1, n + 1):
    nums = int(input())
    if nums > maximum1:
        maximum2 = maximum1
        maximum1 = nums
    elif nums > maximum2:
        minimum2 = nums

print(maximum1)
print(maximum2)
