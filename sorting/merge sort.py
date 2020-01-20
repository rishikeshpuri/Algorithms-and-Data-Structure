def MergeSort(A):
    if len(A)> 1:
        mid = len(A)//2
        leflhalf = A[:mid]
        righthalf = A[mid:]
        MergeSort(leflhalf)
        MergeSort(righthalf)
        i = j = k = 0
        while i<len(leflhalf) and j<len(righthalf):
            if leflhalf[i] < righthalf[j]:
                A[k]=leflhalf[i]
                i=i+1

            else:
                A[k]=righthalf[j]
                j=j+1
            k = k+1
        while i<len(leflhalf):
            A[k]=leflhalf[i]
            i=i+ 1
            k=k+1

        while j<len(righthalf):
            A[k]=righthalf[j]
            j=j+1
            k=k+1
A = [534,246,933, 127,277,321,454,565,220]
MergeSort(A)
print(A)
[127, 127, 220, 220, 220, 565, 220, 565, 220]