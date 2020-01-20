def twoElementsWithSumKBruteForce(A):
    A.sort()
    for i in range(0, len(A)):
        A[i]==A[i]*A[i]
    for j in range(0, i-1):
        A[j] == A[j] * A[j]

    for k in range(0, i-1):
        A[k] == A[k] * A[k]

    