#!/bin/env python3


def check():
    age = int(input())
    if (age % 4 == 0) and ((age % 400 == 0) or (age % 100 != 0)):
        print("YES")
    else:
        print("NO")


def main():
    check()


if __name__ == "__main__":
    main()
