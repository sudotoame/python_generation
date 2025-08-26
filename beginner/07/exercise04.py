def main():
    num = int(input())

    lastdigit = num % 10
    middigit = (num % 100) // 10
    firstdigit = (num % 1000) // 100

    if (lastdigit - firstdigit) == middigit:
        print("Число интересное")
    elif (firstdigit - lastdigit) == middigit:
        print("Число интересное")
    elif (lastdigit + firstdigit) == middigit:
        print("Число интересное")
    elif (firstdigit + lastdigit) == middigit:
        print("Число интересное")
    else:
        print("Число неинтересное")


if __name__ == "__main__":
    main()
