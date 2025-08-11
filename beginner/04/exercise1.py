def is_password():
    pass1, pass2 = input(), input()

    if pass1 != pass2:
        print("Пароль не принят")
    else:
        print("Пароль принят")


def main():
    is_password()


if __name__ == "__main__":
    main()
