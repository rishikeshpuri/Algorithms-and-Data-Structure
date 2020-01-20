def twoElemenlsClosestToZero(A):
    n = len(A)
    if(n < 2):
        print("Tnvabd Input.")
        return
    minLeft = 0
    minRight = 1
    minSum = A[0] + A[1]
    for i in range(0,n-1):

        for r in range(i+1,n):
            sum = A[i] + A[r]
            if(abs(minSum) > abs(sum)):
                minSum = sum
                minLeft = i
                minRight = r
    print(" The two elements whose sum is minimum are", A[minLeft], A[minRight])
A = [1, 60, -10, 70, -80, 85]
twoElemenlsClosestToZero(A)


def twoElemenlsClosestToZero(A):
    n = len(A)
    A.sort()
    if(n < 2):
        print("Invalid Input")
        return
    i= 0
    r = n-1
    minLeft =1
    minRight = n-1
    minSum = 10**9
    while (i<r):
        sum = A[i] + A[r]
        if(abs(minSum) > abs(sum)):
            minSum =sum
            minLeft = i
            minRight = r
        if sum< 0:
            i+= 1
        else:
            r -= 1
    print(" The two clements whose sum is minimum arc", A[minLeft], A[minRight])
A = [1, 60, -10, 70, -80, 85]
twoElemenlsClosestToZero(A)
A=[10,8,3,5,-9,-7,6]
twoElemenlsClosestToZero(A)
