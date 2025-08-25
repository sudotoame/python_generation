def main():
    age = float(input())

    if (age == 1) or (age == 2):
        if age == 1:
            age = 10.5
            print(age)
        elif age == 2:
            age = 21
            print(age)
    else:
        age_a = 21 + (age - 2) * 4
        print(age_a)


if __name__ == "__main__":
    main()
