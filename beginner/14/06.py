text = input()
is_digit = False

for i in range(len(text)):
    if text[i].isdigit() == True:
        is_digit = True

if is_digit is True:
    print("Цифра")
else:
    print("Цифр нет")
