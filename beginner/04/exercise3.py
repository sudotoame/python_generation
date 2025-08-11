def wtf():
    num = int(input())
    a4 = num % 10
    a3 = (num % 100) // 10
    a2 = (num % 1000) // 100
    a1 = (num % 10000) // 1000
    res1 = a1 + a4
    res2 = a2 - a3

    if res1 == res2:
        print("ДА")
    else:
        print("НЕТ")


def main():
    wtf()


if __name__ == "__main__":
    main()
