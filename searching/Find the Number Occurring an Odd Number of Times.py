def repeatingumber(n):
    max=0
    for i in range(0, len(n)):
        count=1
        for j in range(i+1, len(n)):
            if n[i]==n[j]:
                count+=1
        if count % 2 != 0:
            print (n[i])


A=[1,2,3,2, 3, 1,2,3]
repeatingumber(A)

print('---------------')

def getOddOccurrence(arr, arr_size):
    for i in range(0, arr_size):
        count = 0
        for j in range(0, arr_size):
            if arr[i] == arr[j]:
                count += 1

        if (count % 2 != 0):
            return arr[i]

    return -1


# driver code
arr = [1,2,3,2, 3, 1,2,3]
n = len(arr)
print(getOddOccurrence(arr, n))