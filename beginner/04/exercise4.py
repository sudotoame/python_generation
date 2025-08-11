def access():
    age = int(input())
    if age < 18:
        print("Доступ запрещен")
    else:
        print("Доступ разрешен")


def main():
    access()


if __name__ == "__main__":
    main()
