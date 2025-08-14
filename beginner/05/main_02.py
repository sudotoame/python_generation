#!/bin/env python3


def check():
    city = input("В каком городе вы живете?: ")

    if city == "Москва" or city == "Санкт-Петербург" or city == "Екатеринбург":
        print("Доступ разрешен")
    else:
        print("Доступ запрещен")


def main():
    check()


if __name__ == "__main__":
    main()
