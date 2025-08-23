#!/usr/bin/env python3


def main():
    a = int(input())

    if a < 60:
        print("Легкий вес")
    elif a < 64:
        print("Первый полусредний вес")
    elif a < 69:
        print("Полусредний вес")


if __name__ == "__main__":
    main()
