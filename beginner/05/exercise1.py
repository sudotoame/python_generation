#!/bin/env python3


def check():
    num = int(input())

    if num > -1 and num < 17:
        print("Принадлежит")
    else:
        print("Не принадлежит")


def main():
    check()


if __name__ == "__main__":
    main()
