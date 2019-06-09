class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    # tambah data di awal
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False

        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous is None:
            previous = current.getNext()
        else:
            previous.setNext(current.getNext())

    # tambah data di akhir
    # time complexity nya o(n)
    def append(self, item):
        current = self.head
        last = False

        if self.isEmpty():
            self.add(item)
        else:
            while not last:
                if current.getNext() is None:
                    newdata = Node(item)
                    current.setNext(newdata)
                    last = True
                else:
                    current = current.getNext()


if __name__ == '__main__':
    # # sample usage node class
    # node = Node(10)
    # node.setNext(Node(11))
    # print(node.getData())
    # next_node = node.getNext()
    # print(next_node.getData())

    mylist = UnorderedList()
    # mylist.add(10)
    # mylist.add(20)
    # mylist.add(15)

    mylist.append(13)
    mylist.append(10)

    # listing data
    node = mylist.head
    for _ in range(mylist.size()):
        print(node.getData())
        node = node.getNext()
