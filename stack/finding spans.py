def calculateSpan(price, n, s):

    s[0] = 1
    for i in range(1, n):
        s[i] = 1
        j = i-1
        while j >=0 and price[i] >= price[j]:
            s[i]+=1
            j-=1
    return s
p = [10, 4, 5, 90, 120, 80]
n = len(p)
s = [0]*n
x = calculateSpan(p, n, s)
print(x)

# 2nd METHOD

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def isEmpty(self):
        return self.items == []
    def __str__(self):
        return str(self.items)

def findingSpans(A):
    d = Stack()
    s = [0]*len(A)
    for i in range(0, len(A)):
        while not d.isEmpty() and A[i] >= A[d.peek()]:
            d.pop()
        if d.isEmpty():
            p=-1
        else:
            p = d.peek()
        s[i] = i - p
        d.push(i)
    print(s)
A = [10, 4, 5, 90, 120, 80]
findingSpans(A)
