#!/bin/env python3


def check():
    x = int(input())

    if (x >= 1000 and x <= 9999) and ((x % 17 == 0 or x % 7 == 0)):
        print("YES")
    else:
        print("NO")


def main():
    check()


if __name__ == "__main__":
    main()
