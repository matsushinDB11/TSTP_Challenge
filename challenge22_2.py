class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return not self._items

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def size(self):
        return len(self._items)


def reverse_string(value):
    stack = Stack()
    for num in value:
        stack.push(num)
    list_num = len(stack._items)
    re_value = ""
    for i in range(list_num):
        re_value += stack.pop()
    return re_value

if __name__ == '__main__':
    target = "dog"
    r = reverse_string(target)
    print(target, 'を逆から読むと', r)
