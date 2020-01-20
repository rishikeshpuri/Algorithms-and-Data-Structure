class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def display(self):
        for data in reversed(self.items):
            print(data)
        # print( self.items)


def insert_at_bottom(stack, data):
    if stack.is_empty():
        stack.push(data)
    else:
        temp = stack.pop()
        insert_at_bottom(stack, data)
        stack.push(temp)


def reverse_stack(stack):
    if not stack.is_empty():
        temp = stack.pop()
        reverse_stack(stack)
        insert_at_bottom(stack, temp)

s = Stack()
s.push(1)
s.push(2)
s.push(3)

# data_list = input('Please enter the elements to push: ').split()
# for data in data_list:
#     s.push(int(data))

print('The stack:')
s.display()
reverse_stack(s)
print('After reversing:')
s.display()