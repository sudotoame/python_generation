#!/usr/bin/env python3


def main():
    a = int(input())

    if a == 0:
        print("зеленый")
    elif a >= 1 and a <= 10:
        if a % 2 == 0:
            print("черный")
        else:
            print("красный")
    elif a >= 11 and a <= 18:
        if a % 2 == 0:
            print("красный")
        else:
            print("черный")
    elif a >= 19 and a <= 28:
        if a % 2 == 0:
            print("черный")
        else:
            print("красный")
    elif a >= 29 and a <= 36:
        if a % 2 == 0:
            print("красный")
        else:
            print("черный")
    else:
        print("ошибка ввода")


if __name__ == "__main__":
    main()
