class Stack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.arr = []
        self.temp = 0

    def push1(self, data):
        self.stack1.append(data)

    def push2(self, data):
        self.stack2.append(data)


    def pop1(self):
        self.stack1.pop()
        self.stack2.pop()

    def pop2(self):
        self.stack2.pop()

    def get_element(self):
        print(self.stack1)
        print(self.stack2)

    def intersection(self):
        i=0
        j=0
        while i <len(self.stack1):
            while j < len(self.stack2):
                if self.stack1[i] == self.stack2[j]:
                    self.pop1()
                    self.pop2()
                    self.temp = self.pop1()

                else:
                    print( self.temp)
                i += 1
                j += 1



e = Stack()
e.push1(1)
e.push1(2)
e.push1(3)
e.push1(4)
e.push1(5)
e.push1(6)

e.push2(9)
e.push2(11)
e.push2(4)
e.push2(5)
e.push2(6)

e.get_element()

e.intersection()

