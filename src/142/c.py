def main():
    n = int(input())
    a = [int(x) for x in input().strip().split()]
    b = [x for x in range(1, n + 1)]

    _, r = zip(*sorted(zip(a, b)))
    print(*r)


if __name__ == "__main__":
    main()
