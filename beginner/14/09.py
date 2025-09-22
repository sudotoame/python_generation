text = input().lower()

count_a = 0
count_b = 0
a = "ауоыиэяюе"
b = "бвгджзйклмнпрстфхцчшщ"

for i in range(len(text)):
    if text[i] in a:
        count_a += 1
    if text[i] in b:
        count_b += 1

print(f"Количество гласных букв равно {count_a}")
print(f"Количество согласных букв равно {count_b}")
