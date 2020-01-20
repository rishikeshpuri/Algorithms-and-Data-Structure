def findPairs(arr1, arr2, n, m, x):
    for i in range(0, n):
        for j in range(0, m):
            if (arr1[i] + arr2[j] == x):
                print(arr1[i], arr2[j])

arr1 = [1, 2, 3, 7, 5, 4]
arr2 = [0, 7, 4, 3, 2, 1]
n = len(arr1)
m = len(arr2)
x = 8
findPairs(arr1, arr2, n, m, x)

# ------BY HASING-------
def findPairs_byHashing(arr1, arr2, n, m, x):
    s = set()
    for i in range(0, n):
        s.add(arr1[i])

    for j in range(0, m):
        if x - arr2[j] in s:
            print(x-arr2[j], arr2[j])


arr1 = [1, 0, -4, 7, 6, 4]
arr2 = [0, 2, 4, -3, 2, 1]
x = 8

n = len(arr1)
m = len(arr2)
print()
findPairs_byHashing(arr1,arr2,n,m,x)