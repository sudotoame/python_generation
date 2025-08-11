def exer():
    a, b, c, d = int(input()), int(input()), int(input()), int(input())
    min_ab = a
    min_cd = c
    if a < b:
        min_ab = a
    else:
        min_ab = b
    if c < d:
        min_cd = c
    else:
        min_cd = d

    if min_ab < min_cd:
        print(min_ab)
    else:
        print(min_cd)


def main():
    exer()


if __name__ == "__main__":
    main()
