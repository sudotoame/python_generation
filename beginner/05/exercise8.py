#!/bin/env python3


def chess():
    a, b, c, d = int(input()), int(input()), int(input()), int(input())
    c_plus = c - 1
    c_minus = c + 1
    d_plus = d + 1
    d_minus = d - 1

    if (a == c or a == c_plus or a == c_minus) and (
        b == d or b == d_plus or b == d_minus
    ):
        print("YES")
    else:
        print("NO")


def main():
    chess()


if __name__ == "__main__":
    main()
