# dalam kasus ini, Parentheses yang digunakan hanya ( dan )
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)


def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False


def my_way(symbolString):
    open_parentheses = symbolString.count('(')
    close_parentheses = symbolString.count(')')
    return open_parentheses == close_parentheses


sample_string = ['((()))', '(()', '(()()()())', '(()((())()))']
for string in sample_string:
    result = parChecker(string)
    result_my_way = my_way(string)
    print('{}: {}, {}'.format(string, result, result_my_way))
