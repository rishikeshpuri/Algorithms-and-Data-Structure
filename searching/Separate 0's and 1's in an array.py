def seperateEvenOdd(A):
    left = 0
    right = len(A)-1
    while left<right:
        while (A[left] == 0) and left < right:
            left+=1
        while (A[right] == 1) and left< right:
            right -=1
        if left<right:
            # A[left] = A[right]
            # A[right] = A[left]
            A[left], A[right] = A[right], A[left]
            left+=1
            right-=1
A = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
(seperateEvenOdd(A))
print(A)

def rearrangeEvenAndOdd(arr, n):
    j = -1
    for i in range(0, n):
        if (arr[i] == 0):
            j = j + 1
            # swap the element
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
n = len(arr)
rearrangeEvenAndOdd(arr, n)

for i in range(0, n):
    print(arr[i], end=" ")