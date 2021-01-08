import charenge21_1


def reverse_array(x):
    stack = charenge21_1.Stack()
    for num in x:
        stack.push(num)
    list_num = len(stack.items)
    re_list = []
    for i in range(list_num):
        re_list.append(stack.pop())
    return re_list


if __name__ == '__main__':
    list_1 = [1, 2, 3, 4, 5]
    list_2 = reverse_array(list_1)
    print(list_2)
