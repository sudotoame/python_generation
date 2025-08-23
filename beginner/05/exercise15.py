#!/usr/bin/env python3


def main():
    a, b = input(), input()

    if a == "красный" and b == "синий" or a == "синий" and b == "красный":
        print("фиолетовый")
    elif a == "красный" and b == "желтый" or a == "желтый" and b == "красный":
        print("оранжевый")
    elif a == "синий" and b == "желтый" or a == "желтый" and b == "синий":
        print("зеленый")
    elif a == "красный" or a == "синий" or a == "желтный" and a == b:
        print(a)
    else:
        print("ошибка цвета")


if __name__ == "__main__":
    main()
