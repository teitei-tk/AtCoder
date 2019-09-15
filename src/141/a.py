def main():
    s = input()
    weathers = ['Sunny', 'Cloudy', 'Rainy']
    length = weathers.__len__()
    index = weathers.index(s) + 1

    if index >= length:
        index = 0

    print(weathers[index])


if __name__ == "__main__":
    main()
