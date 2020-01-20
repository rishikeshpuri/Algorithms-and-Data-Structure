class Queue:
    def __init__(self, size):
        self.queue = [None]*size
        self.size = size
        self.front = -1
        self.rear = -1

    def enque(self, data):

        if self.front == -1 and self.rear == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = data

        elif self.rear == (self.size-1):
            print('overflow')
            return
        else:
            self.rear += 1
            self.queue[self.rear] = data

    def dequeue(self):
        if self.front == -1 and self.rear == -1:
            print('underflow')
        elif self.front == self.rear:
            print('The dequed element from queue is: ',self.queue[self.front])
            self.front=self.rear = -1
        else:
            print('The dequed element from queue is: ',self.queue[self.front])
            self.front +=1

    def display(self):
        if self.front == -1 and self.rear == -1:
            print('queue is empty')
        else:
            for i in range(self.front, self.rear+1):
                print(self.queue[i])
                i+=1

    def peek(self):
        if self.front == -1 and self.rear == -1:
            print('queue is empty')
        else:
            print('data at front is :',self.queue[self.front])

q = Queue(5)
q.enque(4)
q.enque(3)
q.enque(2)
q.enque(6)
q.enque(7)
q.display()
q.peek()
print()
q.dequeue()
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.dequeue()
q.display()
q.enque(1)
