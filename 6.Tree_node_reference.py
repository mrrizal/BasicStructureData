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


def sample():
    # example usage
    r = BinaryTree('a')
    print(r.getRootVal())
    print(r.getLeftChild())
    r.insertLeft('b')
    print(r.getLeftChild())
    print(r.getLeftChild().getRootVal())
    r.insertRight('c')
    print(r.getRightChild())
    print(r.getRightChild().getRootVal())
    r.getRightChild().setRootVal('hello')
    print(r.getRightChild().getRootVal())


def buildTree():
    r = BinaryTree('a')
    r.insertLeft('b')
    r.insertRight('c')

    left = r.getLeftChild()
    left.insertRight('d')

    right = r.getRightChild()
    right.insertLeft('e')
    right.insertRight('f')

    return r


if __name__ == '__main__':
    ttree = buildTree()

    # test tree object
    print(ttree.getRightChild().getRootVal() == 'c')
    print(ttree.getLeftChild().getRightChild().getRootVal() == 'd')
    print(ttree.getRightChild().getLeftChild().getRootVal() == 'e')
