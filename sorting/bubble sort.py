def BubbleSort( A ):
    for i in range( len( A) ):
        for k in range( len( A) - 1, i, - 1 ):
            if ( A[k] < A[k - 1 ] ):
                swap(A, k, k - 1)

def swap( A, x, y ):
    temp= A[x]
    A[x] = A[y]
    A[y] = temp
A = [534,246,933, 127,277,321,454,565,220]
BubbleSort(A)
print( A)

def BubbleSort1( A ):
    for i in range( 0, len( A) ):
        for k in range( 0, len(A)-1-i ):
            if ( A[k] > A[k + 1 ] ):
                swap1(A, k, k + 1)

def swap1( A, x, y ):
    temp= A[x]
    A[x] = A[y]
    A[y] = temp
A = [534,246,933, 127,277,321,454,565,220]
BubbleSort1(A)
print( A)
