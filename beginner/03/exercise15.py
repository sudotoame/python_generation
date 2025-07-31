num = int(input())

n1 = num % 10
n2 = (num % 100) // 10
n3 = (num % 1000) // 100

sum = n1 + n2 + n3
mul = n1 * n2 * n3

print('Сумма цифр =', sum)
print('Произведение цифр =', mul)
