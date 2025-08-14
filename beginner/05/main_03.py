#!/bin/env python3


def is_not():
    age = int(input("Сколько вам лет?: "))
    if not age < 12:
        print("Доступ разрешен")
    else:
        print("Доступ запрещен")


def isn_not():
    age = int(input("Сколько вам лет?: "))
    if age >= 12:
        print("Доступ разрешен")
    else:
        print("Доступ запрещен")


def main():
    is_not()
    isn_not()


if __name__ == "__main__":
    main()
