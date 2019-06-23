# source: https://runestone.academy/runestone/static/pythonds/Trees/ParseTree.html
class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def parse_tree(string):
    string = list(string)
    stack = Stack()
    tree = BinaryTree('')
    stack.push(tree)
    current_tree = tree

    for char in string:
        if char == '(':
            current_tree.insertLeft('')
            stack.push(current_tree)
            current_tree = current_tree.getLeftChild()

        elif char in ['+', '-', '/', '*']:
            current_tree.setRootVal(char)
            current_tree.insertRight('')
            stack.push(current_tree)
            current_tree = current_tree.getRightChild()

        elif char == ')':
            current_tree = stack.pop()

        elif char.isdigit():
            current_tree.setRootVal(char)
            parent = stack.pop()
            current_tree = parent

    return tree


if __name__ == '__main__':
    tree = parse_tree('((7+3)*(5-2))')

    print(tree.getRootVal() == '*')

    print(tree.getLeftChild().getRootVal() == '+')
    print(tree.getRightChild().getRootVal() == '-')

    print(tree.getLeftChild().getLeftChild().getRootVal() == '7')
    print(tree.getLeftChild().getRightChild().getRootVal() == '3')

    print(tree.getRightChild().getLeftChild().getRootVal() == '5')
    print(tree.getRightChild().getRightChild().getRootVal() == '2')
