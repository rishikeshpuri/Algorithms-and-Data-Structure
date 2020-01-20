def twoElementsWithSumKBruteForce(A, K):

    n = len(A)
    for i in range(0,n):
        for j in range(i+ 1 ,n):
            if(A[i] + A[j] == K):
                return A[i],A[j]
    return 0
A= [1, 4, 45, 6, 10, -8]

print(twoElementsWithSumKBruteForce(A, 16))


def twoElementsWithSumKBruteForce(A, K):
    loIndex = 0
    hiIndex = len(A)- 1;
    while (True):
        if(A[loIndex] + A[hiIndex] == K):
            return 1
        elif(A[loIndex] + A[hiIndex] < K):
            loIndex += 1
        else:
            hiIndex-= 1
    return 0
A = [1, 4, 45, 6, 10, -8]
A.sort()
print(twoElementsWithSumKBruteForce(A, 11))
