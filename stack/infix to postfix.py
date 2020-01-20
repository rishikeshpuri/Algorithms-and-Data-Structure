class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return (self.items == [])
    def peek(self):
        return self.items[-1]
    def __str__(self):
        return str(self.items)

def infixToPostfix(infixexpre):
    prec = {}
    prec['^'] = 4
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1


    opStack = Stack()
    postfixlist = []
    # BY SPLIT
    tokenList = infixexpre.split()
    # WITHOUT SPLIT
    # tokenList = infixexpre
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixlist.append(token)
        elif token == "(":
            opStack.push(token)
        elif token == ")":
            topToken = opStack.pop()
            while topToken != '(':
                postfixlist.append(topToken)
                topToken = opStack.pop()
        else:
            while not opStack.isEmpty() and prec[opStack.peek()] >= prec[token]:
                postfixlist.append(opStack.pop())
            opStack.push(token)
    while not opStack.isEmpty():
        postfixlist.append(opStack.pop())
    return " ".join(postfixlist)

# BY SPLIT
print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("A * ^ B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))

# WITHOUT SPLIT
# print(infixToPostfix("A*B+C*D"))