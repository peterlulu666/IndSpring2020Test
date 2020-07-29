def bottle(num_bottle, num_change):
    total = 0
    bottle_remainder = 0
    while num_bottle:
        total = total + num_bottle
        num_bottle = (num_bottle + bottle_remainder) // num_change
        bottle_remainder = num_bottle % num_change
    return total


def main():
    print(bottle(9, 3))
    print(bottle(15, 4))
    print(bottle(5, 5))
    print(bottle(2, 3))


main()

