number_1 = int(input('Enter first number> '))
number_2 = int(input('Enter second number> '))


def main():
    x = 1

    while True:
        if number_1 * x == number_2 * x:
            print(number_1 * x)
            break
        else:
            x = x+1


main()