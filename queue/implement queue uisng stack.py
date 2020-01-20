class Queue:
    def __init__(self):
        self.stk1 = []
        self.stk2 = []

    def enqueue(self, item):
        while len(self.stk1) != 0:
            self.stk2.append(self.stk1[-1])
            self.stk1.pop()
        self.stk1.append(item)

        while len(self.stk2) != 0:
            self.stk1.append(self.stk2[-1])
            self.stk2.pop()
    def dequeue(self):
        if len(self.stk1)==0:
            print('queue is empty')
        x = self.stk1.pop()
        print('the deleted item from front of queue is :', x)
    def get(self):
        return self.stk1

# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# print(q.get())
#
# q.dequeue()
# print(q.get())

# -----------------OR-----------------
class Queue1:
    def __init__(self):
        self.stk1 = []
        self.stk2 = []
    def enqueue(self, data):
        self.stk1.append(data)

    def dequeue(self):
        if self.stk1 == [] and self.stk2 == []:
            print('empty')
            return
        if self.stk2 == []:

            while len(self.stk1) != 0:
                self.stk2.append(self.stk1[-1])
                self.stk1.pop()

        x = self.stk2.pop()
        print('the deleted item from front of queue is :', x)

        while len(self.stk2) != 0:
            self.stk1.append(self.stk2[-1])
            self.stk2.pop()

    def get(self):
        return self.stk1

q = Queue1()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.get())

q.dequeue()
print(q.get())
