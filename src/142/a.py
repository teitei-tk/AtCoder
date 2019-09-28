def main():
    n = int(input())
    l = [x for x in range(1, n + 1) if x % 2 == 1]
    print(l.__len__() / n)


if __name__ == "__main__":
    main()
