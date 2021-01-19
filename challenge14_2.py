def two_parameter(x, y):
    return x is y


if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    print(two_parameter(list1, list1))
    print(two_parameter(list1, list2))
