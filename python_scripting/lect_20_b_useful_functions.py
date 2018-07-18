def mean(num_list):
    return sum(num_list)/len(num_list)


def add_five(num_list):
    return [num+5 for num in num_list]


def main():
    print("\n Testing mean function\n")

    n_list = [34, 44, 23, 46, 12, 24]
    correct_mean = 30.5
    assert(mean(n_list) == correct_mean)

    print("\n Testing Add Five function\n")

    correct_list = [39, 49, 28, 51, 17, 29]
    assert(add_five(n_list) == correct_list)

    print("\n All tests passed!")


if __name__ == '__main__':
    main()
