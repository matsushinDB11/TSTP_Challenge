class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("""{} by {}
              """.format(self.width,
                         self.len))


class Square(Shape):
    # 問1
    square_list = []

    def __init__(self, w, l):
        self.width = w
        self.len = l
        self.square_list.append(self)

    def area(self):
        return self.width * self.len
    
    # 問2
    def print_size(self):
        print(""" {} by {} by {} by {}
            """.format(self.width,
                       self.len, self.width, self.len))


if __name__ == '__main__':
    square_one = Square(20, 20)
    square_two = Square(29, 29)
    print(Square.square_list)
    square_one.print_size()
    square_two.print_size()
