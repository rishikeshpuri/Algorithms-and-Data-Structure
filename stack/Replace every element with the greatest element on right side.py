def nextGreatest(arr):
    size = len(arr) - 1
    max_from_right = arr[size]

    arr[size] = -1
    for i in range(size-1, -1, -1):
        temp = arr[i]
        arr[i] = max_from_right
        if max_from_right < temp:
            max_from_right = temp

arr = [16, 17, 4, 3, 5, 2]
(nextGreatest(arr))
print("Modified array is", (arr))

