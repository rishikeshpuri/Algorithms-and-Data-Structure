class Stack(object):
    def __init__(self, limit):
        self.limit = limit
        self.stk = []

    def isEmpty(self):
        if len(self.stk) <= 0:
            print("Stack Empty")

    def push(self, item):
        if len(self.stk) >= self.limit:
            print("Stack OverFlow")
        else:
            self.stk.append(item)
            print('Stack after Push', self.stk)

    def isFullStack(self):
        if len(self.stk) >= self.limit:
            print("Stack Full")

    def pop(self):
        if len(self.stk) <= 0:
            print("Stack UnderFlow")
        else:
            return self.stk.pop()

    def peek(self):
        if len(self.stk) <= 0:
            print("Stack UnderFlow")
        else:
            return self.stk[-1]

    def size(self):
        return len(self.stk)

    def get_item_in_stk(self):
        return self.stk

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


def inlcrLeavingQueuc(que):
    stk = Stack(9)
    halfSize = que.size// 2
    for i in range(0,halfSize):
        stk. push(que.dequeue())

    while not stk.isEmpty():
        que.enque(stk. pop())

    for i in range(0,halfSize):
        que.enque(que.dequeue())

    for i in range(0,halfSize):
        stk.push(que.dequeue())

    while not stk.isEmpty():
        que.enque(stk.pop())
        que.enque(que.dequeue())

que = Queue(10)

que.enque(11)
que.enque(12)
que.enque(13)
que.enque(14)
que.enque(15)
que.enque(16)
que.enque(17)
que.display()
inlcrLeavingQueuc(que)
