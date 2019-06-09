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


class OrderedList:
    def __init__(self):
        self.head = None

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
        stop = False

        while current is not None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

    def add(self, item):
        current = self.head
        previous = None
        stop = False

        while current is not None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        # if previous kosong, berarti nambah data dilakukan di depan
        if previous is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)


if __name__ == '__main__':
    mylist = OrderedList()
    # add data to ordered link list
    for i in range(10, 0, -1):
        mylist.add(i)

    # listing data
    node = mylist.head
    for _ in range(mylist.size()):
        print(node.getData())
        node = node.getNext()
