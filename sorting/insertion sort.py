def Insertionsort( A ):
    for i in range( 1 , len( A ) ):
        temp = A[i]
        k= i
        while k > 0 and temp< A[k - 1 ]:
            A[k] = A[k - 1]
            k -= 1
        A[k] =temp
A = [6, 8, 4, 5, 3, 7, 2]
Insertionsort(A)
print(A)
