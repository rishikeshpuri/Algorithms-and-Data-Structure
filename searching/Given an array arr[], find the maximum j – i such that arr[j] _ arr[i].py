def maxIndexDiff(arr, n):
    maxDiff = -1
    for i in range(0, n):
        j = n - 1
        while (j > i):
            if arr[j] > arr[i] and maxDiff < (j - i):
                maxDiff = j - i

            j -= 1


    return maxDiff

arr = [9, 2, 3, 4, 5, 6, 7, 8, 18, 0]
n = len(arr)
maxDiff = maxIndexDiff(arr, n)
print(maxDiff)