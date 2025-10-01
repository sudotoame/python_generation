num = int(input())

text = ""

while num > 0:
    text = str(num % 2) + text
    num //= 2

print(text)
