class SmartStack:
    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def push(self, data):
        self.main_stack.append(data)
        if len(self.min_stack) != 0 and data <= self.min_stack[-1]:
            self.min_stack.append(data)
        elif len(self.min_stack) == 0:
            self.min_stack.append(data)

    def pop(self):
        if len(self.main_stack) == 0:
            return None

        else:
            if self.main_stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            return self.main_stack.pop()


    def top(self):
        if len(self.main_stack) == 0 :
            return None
        else:
            return self.main_stack[-1]


    def get_Minimum(self):
        if len(self.min_stack) == 0:
            return None
        else:
            return self.min_stack[-1]

    def get_Mainstack(self):
        return self.main_stack

    def get_Minstack(self):
        return self.min_stack

myStack = SmartStack()
myStack.push(5)
myStack.push(3)
myStack.push(9)
myStack.push(0)
myStack.push(-1)
myStack.push(10)
# myStack.push(11)
print(myStack.get_Mainstack())
print(myStack.get_Minstack())
print()
myStack.pop()
myStack.pop()
# myStack.push(5)
# myStack.push(5)
print(myStack.get_Mainstack())
print(myStack.get_Minstack())
print(myStack.get_Minimum())