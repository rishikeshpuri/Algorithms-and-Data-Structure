class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def enQueue(self, data):
        self.queue.append(data)

    def deQueue(self):
        if self.queue:
            a = self.queue[0]
            self.queue.remove(a)
            return a
        else:
            raise IndexError('quere is empty')

    def size(self):
        return len(self.queue)

class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def isEmpty(self):
        return self.q1.isEmpty() and self.q2.isEmpty()

    def push(self, item):
        if self.q2.isEmpty():
            self.q1.enQueue(item)

        else:
            self.q2.enQueue(item)

    def pop(self):
        if self.isEmpty():
            raise IndexError('stack is empty')
        elif self.q2.isEmpty():
            while not self.q1.isEmpty():
                cur = self.q1.deQueue()
                if self.q1.isEmpty():
                    return cur
                self.q2.enQueue(cur)
        else:
            while not self.q2.isEmpty():
                cur = self.q2.deQueue()
                if self.q2.isEmpty():
                    return cur
                self.q1.enQueue(cur)

stk = Stack()
for i in range(5):
    stk.push(i)

for i in range(5):
    stk.pop()