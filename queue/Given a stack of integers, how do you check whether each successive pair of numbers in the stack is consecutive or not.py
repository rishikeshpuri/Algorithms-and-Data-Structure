def pairWiseConsecutive(stk):
    auxStk = []
    while len(stk)!=0:
        auxStk.append(stk[-1])
        stk.pop()
    result = True
    while len(auxStk)>1:
        x = auxStk[-1]
        auxStk.pop()
        y = auxStk[-1]
        auxStk.pop()

        if abs(x - y) != 1:
            result = False
        stk.append(x)
        stk.append(y)

    if len(auxStk) == 1:
        stk.append(auxStk[-1])
    return result
stk = [4,5,-2,-3,11,10,5,6,20]
s = pairWiseConsecutive(stk)
print(s)
while len(stk)!=0:
    print(stk[-1], end=" ")
    stk.pop()
