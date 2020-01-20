def seperateEvenOdd(A):
    left = 0
    right = len(A)-1
    while left<right:
        while (A[left]%2 == 0) and left < right:
            left+=1
        while (A[right]%2 == 1) and left< right:
            right -=1
        if left<right:
            # A[left] = A[right]
            # A[right] = A[left]
            A[left], A[right] = A[right], A[left]
            left+=1
            right-=1
A = [12, 34, 45, 9, 8, 90, 3]
(seperateEvenOdd(A))
print(A)

# OR

def rearrangeEvenAndOdd(arr, n):
    j = -1
    for i in range(0, n):
        if (arr[i] % 2 == 0):
            j = j + 1
            # swap the element
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
arr = [12, 10, 9, 45, 2, 10, 10, 45]
n = len(arr)
rearrangeEvenAndOdd(arr, n)

for i in range(0, n):
    print(arr[i], end=" ")