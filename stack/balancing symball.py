class Stack(object):
    def __init__(self, limit):
        self.limit = limit
        self.stk = []

    def isEmptyStack(self):
        return len(self.stk) <= 0

    def push(self, item):
        if len(self.stk) >= self.limit:
            print("Stack OverFlow")
        else:
            self.stk.append(item)
            print('Stack after Push', self.stk)

    def isFullStack(self):
        return len(self.stk) >= self.limit

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


def symbolBalance(input):
    symbolStack = Stack(10)
    balance = 0
    for symbol in input:
        if symbol in ["(", "{", "["]:
            symbolStack.push(symbol)
        else:
            if symbolStack.isEmptyStack():
                balance = 0
            else:
                topSymbol = symbolStack.pop()
                if not matches(topSymbol, symbol):
                    balance = 0
                else:
                    balance = 1
    return balance


def matches(p1, p2):
    if p1 == '(' and p2 == ')':
        return True
    elif p1 == '{' and p2 == '}':
        return True
    elif p1 == '[' and p2 == ']':
        return True
    else:
        return False
#
# balance = symbolBalance("(({{}}))")
# print(balance)


#      OR ---2ND METHOD----

def is_paranthesis_balanced(paran_string):
    s =Stack(10)
    is_balanced = True
    index = 0
    while index < len(paran_string) and is_balanced:
        paren = paran_string[index]
        if paren in "({[":
            s.push(paren)
        else:
            if s.isEmptyStack():
                is_balanced = False
            else:
                top = s.pop()
                if not matches(top, paren):
                    is_balanced = True
        index+=1
    if s.isEmptyStack() and is_balanced:
        return True
    else:
        return False

paren = is_paranthesis_balanced("(({{}}))")
print(paren)