text = input()
total = 0
while text != "stop":
    total += int(text)
    text = input()
print("Сумма всех чисел: ", total)
