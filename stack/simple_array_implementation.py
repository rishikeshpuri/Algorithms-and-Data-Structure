class Stack(object):
    def __init__(self, limit):
        self.limit = limit
        self.stk = []

    def isEmptyStack(self):
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

our_stack =  Stack(5)

our_stack.push(1)
our_stack.push(2)
our_stack.push(3)
our_stack.push(4)
print(our_stack.pop())
print(our_stack.get_item_in_stk())
print(our_stack.peek())
print(our_stack.get_item_in_stk())

print(our_stack.size())

