class Deque:
    def __init__(self, size):
        self.deQue = [0]*size
        self.front = -1
        self.rear = -1
        self.size = size

    def enqueueFront(self, data):
        if (self.front == 0 and self.rear == self.size - 1) or self.front == self.rear+1:
            print('queue is full or overflow')

        elif self.front == -1 or self.rear == -1:
            self.front = self.rear = 0
            self.deQue[self.front] = data

        elif self.front == 0:
            self.front = self.size -1
            self.deQue[self.front] = data

        else:
            self.front -=1
            self.deQue[self.front] = data

    def enqueueRear(self, data):
        if (self.front == 0 and self.rear == self.size - 1) or self.front == self.rear+1:
            print('queue is full or overflow')

        elif self.front == -1 or self.rear == -1:
            self.front = self.rear = 0
            self.deQue[self.rear] = data

        elif self.rear == self.size-1:
            self.rear = 0
            self.deQue[self.rear] = data

        else:
            self.rear +=1
            self.deQue[self.rear] = data

    def display(self):
        if self.front == -1 and self.rear == -1:
            print('queue is empty')
        i = self.front
        while i != self.rear:
            print(self.deQue[i])
            i = (i+1)% self.size
        print(self.deQue[self.rear])

    def getFront(self):
        if self.front == -1 and self.rear == -1:
            print('queue is empty')
        else:
            print('the FRONT value is: ', self.deQue[self.front])

    def getrear(self):
        if self.front == -1 and self.rear == -1:
            print('queue is empty')
        else:
            print('the REAR value is: ', self.deQue[self.rear])

    def dequeueFront(self):
        if self.front == -1 and self.rear == -1:
            print('queue is empty')

        elif self.front == self.rear:
            print('the deleted value is :', self.deQue[self.front])
            self.front = self.rear = -1

        elif self.front == self.size-1:
            print('the deleted value is :', self.deQue[self.front])
            self.front = 0

        else:
            print('the deleted value is :', self.deQue[self.front])
            self.front = self.front+1

    def dequeueRear(self):
        if self.front == -1 and self.rear == -1:
            print('queue is empty')

        elif self.front == self.rear:
            print('the deleted value is :', self.deQue[self.rear])
            self.front = self.rear = -1

        elif self.rear == 0:
            print('the deleted value is :', self.deQue[self.rear])
            self.rear =self.size - 1

        else:
            print('the deleted value is :', self.deQue[self.rear])
            self.rear -= 1

q = Deque(5)
q.enqueueFront(2)
q.enqueueFront(6)
q.enqueueRear(-1)
q.enqueueRear(8)
q.display()
print()
q.getFront()
q.getrear()
q.dequeueFront()
q.display()
q.dequeueRear()
q.display()
q.dequeueRear()
q.display()
q.dequeueFront()
print()
q.display()
print()
q.getrear()
q.getFront()