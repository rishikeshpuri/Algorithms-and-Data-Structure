class Queue:
    def __init__(self):
        self.stk1 = []
        self.stk2 = []


    def enque(self, item):
        self.stk1.append(item)

    def get2(self):
        print(self.stk2)

    def get1(self):
        print(self.stk1)

    def reverse(self):
        if self.stk1 == [] and self.stk2 == []:
            print('empty')

        if self.stk2 == []:
            while len(self.stk1) != 0:
                self.stk2.append(self.stk1[-1])
                self.stk1.pop()
            print('the reverse of queue is :', self.stk2)


q = Queue()
q.enque(1)
q.enque(2)
q.enque(3)
q.enque(4)
q.enque(5)
q.get1()
q.reverse()


