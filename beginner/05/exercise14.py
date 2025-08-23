#!/usr/bin/env python3


def main():
    a, b, c = int(input()), int(input()), input()

    if c == "/":
        if b == 0:
            print("На ноль делить нельзя!")
        else:
            print(a / b)
    elif c == "+":
        print(a + b)
    elif c == "-":
        print(a - b)
    elif c == "*":
        print(a * b)
    else:
        print("Неверная операция")


if __name__ == "__main__":
    main()
