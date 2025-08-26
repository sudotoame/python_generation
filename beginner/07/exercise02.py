#!/usr/bin/env python3


def main():
    a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())

    maximum = max(a, b, c, d, e)
    minimum = min(a, b, c, d, e)

    print("Наименьшее число =", minimum)
    print("Наибольшее число =", maximum)


if __name__ == "__main__":
    main()
