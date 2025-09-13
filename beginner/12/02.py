counter1 = 0
counter2 = 0

for _ in range(10):
    num = int(input())
    if num > 10:
        counter1 += 1
    elif num == 0:
        counter2 += 1

print(f'Было введено {counter1} чисел, больше 10')
print(f'Было введено {counter2} числе, равных нулю')
