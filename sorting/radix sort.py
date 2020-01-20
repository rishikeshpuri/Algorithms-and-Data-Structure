def countingSort(A, pos):
    B = [0 for el in A]
    c = [0 for el in range(10)]

    for i in range(0, len(A)):
        index = A[i]//pos
        c[index % 10] +=1

    for j in range(1, 10):
        c[j] += c[j-1]

    i = len(A)-1
    while i>=0:
        index = A[i]//pos
        B[c[index % 10] -1] = A[i]
        c[index %10] -= 1
        i -= 1
    for j in range(0, len(A)):
        A[j] = B[j]

def radixSort(A):

    m = max(A)
    pos = 1

    while m/pos > 0:
        countingSort(A,pos)
        pos = pos *10
A = [ 170, 45, 75, 90, 802, 24, 2, 66]
radixSort(A)
print(A)
