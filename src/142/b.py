def main():
    l = input().strip().split(" ")
    n = int(l[0])
    k = int(l[1])

    h = [int(x) for x in input().strip().split(" ", n)]

    count = 0
    for x in h:
        if not x >= k:
            continue
        count += 1

    print(count)


if __name__ == "__main__":
    main()
