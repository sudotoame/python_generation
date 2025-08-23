#!/usr/bin/env python3


def main():
    n, k = int(input()), int(input())

    if n > k:
        print("NO")
    elif n < k:
        print("YES")
    else:
        print("Don't know")


if __name__ == "__main__":
    main()
