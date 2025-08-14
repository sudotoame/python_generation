#!/bin/env python3


def check():
    x = int(input())

    if (x > -30 and x <= -2) or (x > 7 and x <= 25):
        print("Принадлежит")
    else:
        print("Не принадлежит")


def main():
    check()


if __name__ == "__main__":
    main()
