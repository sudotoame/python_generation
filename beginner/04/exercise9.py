def sum_positive():
    a, b, c = int(input()), int(input()), int(input())
    sum = 0
    if a >= 0:
        sum += a
    if b >= 0:
        sum += b
    if c >= 0:
        sum += c

    print(sum)


def main():
    sum_positive()


if __name__ == "__main__":
    main()
