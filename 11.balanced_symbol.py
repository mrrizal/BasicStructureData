# dalam kasus ini, simbol yang digunakan adalah ({ dan [
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


def matches(open_, close):
    opens = '({['
    closes = ')}]'

    return opens.index(open_) == closes.index(close)


def parChecker(symbol_string):
    s = Stack()
    balanced = True
    index = 0

    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]

        if symbol in '({[':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False

        index += 1

    if balanced and s.isEmpty():
        balanced = True
    else:
        balanced = False

    return balanced


samples = ['{{([][])}()}', '[{()]', '{{([][])}()}', '([)]']

for sample in samples:
    result = parChecker(sample)
    print('{}: {}'.format(sample, result))
