def sort012(A):
    lo = 0
    hi = len(A) - 1
    mid = 0
    while mid <= hi:
        if A[mid] == 0:
            A[lo], A[mid] = A[mid], A[lo]
            lo = lo + 1
            mid = mid + 1
        elif A[mid] == 1:
            mid = mid + 1
        else:
            A[hi], A[mid] = A[mid], A[hi]
            hi = hi - 1
A = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
sort012(A)
print(A)
