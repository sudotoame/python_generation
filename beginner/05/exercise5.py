#!/bin/env python3


def check():
    a, b, c = int(input()), int(input()), int(input())

    if ((a + b) > c) and ((a + c) > b) and ((b + c) > a):
        print("YES")
    else:
        print("NO")


def main():
    check()


if __name__ == "__main__":
    main()
