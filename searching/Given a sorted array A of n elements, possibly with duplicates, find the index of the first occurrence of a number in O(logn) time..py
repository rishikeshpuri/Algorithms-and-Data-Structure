def findFirstOccurance(A, target):
    left = 0
    right = len(A)-1
    lastFound = 1
    while left<=right:
        # if left>right:
        #     return lastFound
        mid = (left+right)//2
        if A[mid] == target:
            lastFound = mid
            right = mid - 1
        elif A[mid] <= target:
            left = mid+1
        else:
            right = mid-1
    return lastFound
A= [4,4,4,4,5, 6, 9, 12, 15,21,21,21, 21, 21, 34, 45, 57, 70, 84]
print(findFirstOccurance(A,5))
