counter = 0

for _ in range(10):
    num = int(input())
    if num > 10:
        counter += 1

print(f'Было введено {counter} чисел, больше 10')
