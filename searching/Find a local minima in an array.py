def localMinima(A):
    left = 0
    right =len(A)-1
    n=len(A)

    while left<=right:
        mid = (left+ right)//2

        if A[mid] == 0 or A[mid-1] > A[mid] and mid == n-1 or A[mid] < A[mid +1]:
            return mid
        elif A[mid] > 0 and A[mid] > A[mid-1]:
            right = mid-1
        elif A[mid] > 0 and A[mid] < A[mid-1]:
            left = mid+1
    return mid
arr = [4, 3, 1, 14, 16, 40]
print("Index of a local minima is " , localMinima(arr))