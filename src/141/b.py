def main():
    odd = False
    even = False

    odds = []
    evens = []
    for i, s in enumerate(list(input())):
        if i % 2 == 0:
            evens.append(s in ['R', 'U', 'D'])
        else:
            odds.append(s in ['L', 'U', 'D'])

    odd = odds.count(False) == 0
    even = evens.count(False) == 0

    r = 'No'
    if odd and even:
        r = 'Yes'

    print(r)


if __name__ == "__main__":
    main()
