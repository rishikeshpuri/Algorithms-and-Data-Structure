class CircularQueue:
    def __init__(self, size):
        self.queue = [None]*size
        self.size = size
        self.front = -1
        self.rear = -1

    def enque(self, data):
        if self.front == -1 and self.rear == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = data

        elif (self.rear +1) % self.size == self.front:
            print('overflow')

        else:
            self.rear = (self.rear+1)%self.size
            self.queue[self.rear] = data

    def dequeue(self):
        if self.front == -1 and self.rear == -1:
            print('underflow')
        elif self.front == self.rear:
            print('The dequed element from queue is: ',self.queue[self.front])
            self.front=self.rear = -1
        else:
            print('The dequed element from queue is: ', self.queue[self.front])
            self.front = (self.front+1) %self.size

    def display(self):
        if self.front == -1 and self.rear == -1:
            print('queue is empty')
        else:
            i = self.front
            while i != self.rear:
                print(self.queue[i])
                i = (i+1)%self.size
            print(self.queue[self.rear])

    def peek(self):
        if self.front == -1 and self.rear == -1:
            print('queue is empty')
        else:
            print('data at front is :', self.queue[self.front])

q = CircularQueue(5)
q.enque(4)
q.enque(3)
q.enque(2)
q.enque(6)
q.enque(7)
q.display()
q.peek()
print()
q.dequeue()
q.dequeue()
q.display()
print()
q.enque(10)
q.enque(0)
q.enque(1)
q.display()