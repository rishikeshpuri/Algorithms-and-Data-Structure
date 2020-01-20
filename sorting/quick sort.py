def PivotPlace(A, low, high):
    pivot = A[low]
    left = low+1
    right = high

    while True:
        while left <= right and A[left] <= pivot:
            left +=1
        while left <= right and A[right] >= pivot:
            right -=1

        if left > right:
            break
        else:
            A[left], A[right] = A[right], A[left]
    A[low], A[right] = A[right], A[low]
    return right

def QuickSort( A, low, high ):

    if low < high:
        pivot = PivotPlace( A, low, high)
        QuickSort( A, low, pivot - 1 )
        QuickSort( A, pivot + 1, high)


A = [10, 7, 8, 9, 1, 5]
QuickSort(A,0, len(A)-1)
print(A)