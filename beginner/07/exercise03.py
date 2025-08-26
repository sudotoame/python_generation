#!/usr/bin/env python3


def main():
    a, b, c = int(input()), int(input()), int(input())
    maximum = max(a, b, c)
    minimum = min(a, b, c)

    if a == maximum:
        print(a)
        if b == minimum:
            print(c)
            print(b)
        else:
            print(b)
            print(c)
    elif b == maximum:
        print(b)
        if a == minimum:
            print(c)
            print(a)
        else:
            print(a)
            print(c)
    elif c == maximum:
        print(c)
        if a == minimum:
            print(b)
            print(a)
        else:
            print(a)
            print(b)
    elif a == b == c:
        print(a)
        print(b)
        print(c)


if __name__ == "__main__":
    main()
