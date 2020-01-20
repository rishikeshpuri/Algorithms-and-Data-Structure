class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front == None

    def enQueue(self, item):
        new_node = Node(item)

        if self.rear == None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def deQueue(self):
        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next
        if self.front == None:
            self.rear = None
        print("Dequeued item is " + str(temp.data))
        return
    def getItem(self):
        current = self.front
        if current == None:
            return
        while current:
            print(current.data, '->', end=' ')
            current = current.next


if __name__ == '__main__':
    q = Queue()
    q.enQueue(10)
    q.enQueue(20)

    q.enQueue(20)
    q.enQueue(38)
    q.enQueue(249)
    q.getItem()
    print()
    q.deQueue()
    print()
    q.getItem()