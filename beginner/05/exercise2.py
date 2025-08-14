#!/bin/env python3


def check():
    x = int(input())

    if x <= -3 or x >= 7:
        print("Принадлежит")
    else:
        print("Не принадлежит")


def main():
    check()


if __name__ == "__main__":
    main()
