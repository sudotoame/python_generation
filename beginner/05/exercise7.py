#!/bin/env python3


def chess():
    a, b, c, d = int(input()), int(input()), int(input()), int(input())

    if (a == c) or (b == d):
        print("YES")
    else:
        print("NO")


def main():
    chess()


if __name__ == "__main__":
    main()
