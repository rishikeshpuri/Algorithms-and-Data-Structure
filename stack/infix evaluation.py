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

def infixEval(infixExpr):
    prec = {}
    prec['^'] = 4
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1

    operandStack = []
    operatorStack = Stack()
    tokenList = infixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.append(int(token))
        elif token == '(':
            operatorStack.push(token)
        elif token == ')':

            while operatorStack.peek() != '(':

                operator = operatorStack.pop()
                operand2 = operandStack.pop()
                operand1 = operandStack.pop()
                result = doMath(operator, operand1, operand2)
                operandStack.append(result)
            operatorStack.pop()
        else:
            while not operatorStack.isEmpty() and prec[operatorStack.peek()] >= prec[token]:
                operator = operatorStack.pop()
                operand2 = operandStack.pop()
                operand1 = operandStack.pop()
                result = doMath(operator, operand1, operand2)
                operandStack.append(result)
            operatorStack.push(token)

    while not operatorStack.isEmpty():
        operator = operatorStack.pop()
        operand2 = operandStack.pop()
        operand1 = operandStack.pop()
        result = doMath(operator, operand1, operand2)
        operandStack.append(result)
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

print(infixEval("5 + 2 * 6"))
print(infixEval("( 5 + 2 ) * 6" ))
# print(infixEval("( 50 + 2 ) * 6 / ( 3 + 4 )" )) # Error

def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0

def applyOp(a, b, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a // b

def evaluate(tokens):
    values = []
    ops = []
    i = 0
    while i < len(tokens):
        if tokens[i] == ' ':
            i += 1
            continue
        elif tokens[i] == '(':
            ops.append(tokens[i])
        elif tokens[i].isdigit():
            val = 0
            while i < len(tokens) and tokens[i].isdigit():
                val = val*10 + int(tokens[i])
                i+=1
            values.append(val)
        elif tokens[i] == ')':
            while len(ops) != 0 and ops[-1] != '(':
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()

                values.append(applyOp(val1, val2, op))
            ops.pop()
        else:
            while (len(ops) != 0 and
                   precedence(ops[-1]) >= precedence(tokens[i])):
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()

                values.append(applyOp(val1, val2, op))

                # Push current token to 'ops'.
            ops.append(tokens[i])

        i += 1
    while len(ops) != 0:
        val2 = values.pop()
        val1 = values.pop()
        op = ops.pop()

        values.append(applyOp(val1, val2, op))

    return values[-1]


print(evaluate(" 10 + 2 * 6"))
print(evaluate("100 * 2 + 12"))