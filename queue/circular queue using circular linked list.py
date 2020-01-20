class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enQueue(self, item):
        new_node = Node(item)
        if self.front ==None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
        new_node.next = self.front

    def deQueue(self):
        if self.front == None:
            print('Queue is empty')
            return
        if self.front == self.rear:
            self.front = None
            return
        temp = self.front
        self.front = temp.next
        self.rear.next = self.front
        print("Dequeued item is " + str(temp.data))

    def peek(self):
        if self.front == None:
            print('Queue is empty')
            return
        print('The first element in queue is :', self.front.data)


    def get_circularLlist(self):
        current = self.front
        while current:
            print(current.data)
            current = current.next
            if current == self.front:
                break

q = CircularQueue()
q.enQueue(5)
q.enQueue(4)
q.enQueue(6)
q.enQueue(8)
q.get_circularLlist()
q.deQueue()
q.get_circularLlist()
q.peek()


q.get_circularLlist()
