class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items)-1
        return self.items[last]

    def size(self):
        return len(self.items)


def reverse_array(x):
    stack = Stack()
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
