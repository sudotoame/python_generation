#!/usr/bin/env python3


def main():
    a1, b1 = int(input()), int(input())
    a2, b2 = int(input()), int(input())

    if b1 < a2 or b2 < a1:
        print("пустое множество")
    elif b1 == a2 or b2 == a1:
        if b1 == a2:
            print(b1)
        else:
            print(b2)
    elif (a1 < a2) < (b1 < b2):
        print(a2, b1)
    elif (a2 < a1) < (b2 < b1):
        print(a1, b2)
    elif (a1 == a2) < (b1 < b2):
        print(a1, b1)
    elif (a1 == a2) < (b2 < b1):
        print(a1, b2)
    elif (a2 < a1 and b1 < b2) or (a1 < a2 and b2 < b1):
        if a2 < a1 and b1 < b2:
            print(a1, b1)
        else:
            print(a2, b2)
    elif (a2 < a1) and (b1 == b2):
        print(a1, b1)
    elif (a1 < a2) and (b1 == b2):
        print(a2, b1)
    elif (a1 == a2) and (b1 == b2):
        print(a1, b2)


if __name__ == "__main__":
    main()
