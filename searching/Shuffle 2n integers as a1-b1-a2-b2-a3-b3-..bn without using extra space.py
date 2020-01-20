def rearrange(A):
    # n = len(arr)

    if (len(A) % 2 == 1):
        return
    currIdx = int((len(A) - 1) / 2)

    while (currIdx > 0):

        count = currIdx
        swapIdx = currIdx

        while (count > 0):
            # temp = A[swapIdx + 1]
            # A[swapIdx + 1] = A[swapIdx]
            # A[swapIdx] = temp
            A[swapIdx], A[swapIdx+1] = A[swapIdx+1], A[swapIdx]
            swapIdx = swapIdx + 1
            count = count - 1

        currIdx = currIdx - 1


A = [1, 3, 5, 2, 4, 6]
rearrange(A)
print(A)