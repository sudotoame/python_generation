#!/usr/bin/env python3


def check():
    age = int(input("Сколько вам лет?: "))
    classes = int(input("В каком классе вы учитесь?: "))
    city = input("В каком городе вы живете: ")

    if age >= 7 and classes >= 7 and (city == "Москва" or city == "Санкт-Петербург"):
        print("Доступ разрешен")
    else:
        print("Доступ запрещен")


def main():
    check()


if __name__ == "__main__":
    main()
