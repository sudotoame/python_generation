text = input()
count_p = 0
count_m = 0

for i in range(len(text)):
    if text[i] == "+":
        count_p += 1
    if text[i] == "*":
        count_m += 1

print(f"Символ + встречается {count_p} раз")
print(f"Символ * встречается {count_m} раз")
