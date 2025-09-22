def main():
    num = int(input())
    count = 0
    for i in range(2, num + 1):
        if num % i == 0:
            print(i)
            break

if __name__ == "__main__":
    main()