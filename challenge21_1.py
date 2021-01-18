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


if __name__ == "__main__":
    text = "yesterday"    

    stack = Stack()
    for char in text:
        stack.push(char)

    reversed_string = ""

    for i in range(len(stack.items)):
        reversed_string += stack.pop()

    print(reversed_string)
