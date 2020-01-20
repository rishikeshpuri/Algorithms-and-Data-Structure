def secondSmallestefficiency(A, target):
    x = A[0]
    count = 0
    # return (x)
    t=0

    for i in range(0, len(A)):
        if A[i]==x:
            count+=1
        # return (count)
    x=count

    if  A[x] == target:
        t = target


    for i in range(0, len(A)):
        targetCount = 0
        if A[i]==t:
           targetCount += 1
        return targetCount
A = [2,2,2, 3,4,4,4,4,5,5,6,7,8]
print(secondSmallestefficiency(A,2))