def if_python():
    answer = input("Какой язык программирования мы учим?: ")
    if answer == "Python":
        print("Верно! Мы ботаем Python!")
        print("Python - отличный язык!")
    elif answer == "python":
        print("Верно! Мы ботаем Python!")
        print("Python - отличный язык!")
    else:
        print("Неверно!!!")


def less_or_great():
    num1 = input("Введите первое число: ")
    num2 = input("Введите второе число: ")

    if num1 < num2:
        print("Первое число меньше чем второе")
    if num1 > num2:
        print("Первое число больше чем второе")
    if num1 == num2:
        print("Числа равны")
    if num1 != num2:
        print("Числа не равны")


def is_child():
    age = int(input())
    if 3 <= age <= 6:
        print("Ты ребенок!")
    else:
        print("Тебе не от 3 до 6 лет")


def is_greatness():
    a, b, c = int(input()), int(input()), int(input())
    if a == b == c:
        print("Числа равны")
    else:
        print("Числа не равны")


def main():
    # if_python()
    # less_or_great()
    # is_child()
    is_greatness()


if __name__ == "__main__":
    main()
