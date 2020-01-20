class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return self.items == []
    def peek(self):
        return self.items[-1]
    def __str__(self):
        return str(self.items)

def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()
    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(result)
    return operandStack.pop()

def doMath(operation, op1, op2):
    if operation == '*':
        return op1 * op2
    elif operation == '/':
        return op1 / op2
    elif operation == '+':
        return op1 + op2
    elif operation == '-':
        return op1 - op2

print(postfixEval('1 2 3 * + 5 -'))
