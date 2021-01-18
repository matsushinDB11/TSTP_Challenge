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


if __name__ == '__main__':
    stack = Stack()
    print("stackは空?", stack.is_empty())
    stack.push(1)
    print("stackは空?", stack.is_empty())
    stack.push(99)
    print("stackの一番上は?", stack.peek())
    print("stackのサイズは?", stack.size())
    print("stackから取り出したのは:", stack.pop())
    print("stackから取り出したのは:", stack.pop())
    print("stackは空?", stack.is_empty())
