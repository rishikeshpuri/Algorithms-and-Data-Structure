# (Naive : O(n^2))

def removeDups(n):
    res_ind = 1
    for i in range(1, len(n)):
        j = 0
        while j<i:
            if n[i] == n[j]:
                break
            j+=1
        if j == i:
            n[res_ind] = n[i]
            res_ind+=1
    return n[0:res_ind]

n = [3, 5, 7, 2, 2, 5, 7, 7]
n = removeDups(n)

for i in range(len(n)):
    print(n[i], end=' ')

# (Naive : O(n))
def remove_duplicates(arr, n):
    if n == 0 or n == 1:
        return n
    temp = list(range(n))
    j = 0
    for i in range(0, n-1):
        if arr[i] !=arr[i+1]:
            temp[j] = arr[i]
            j+=1

    temp[j] = arr[n-1]
    j+=1

    for i in range(0, j):
        arr[i]= temp[i]
    return j

arr = [1, 2, 2, 3, 4, 4, 4, 5, 5,5]
n = len(arr)

n = remove_duplicates(arr, n)
print()
for i in range(n):
    print(arr[i], end='')

# BY HASMAP
# (Naive : O(n))

def remove_by_hasmap(arr):
    mp = {i : 0 for i in arr}

    for i in range(len(arr)):
        if mp[arr[i]] == 0:
            print(arr[i], end = ' ')
            mp[arr[i]] = 1

arr = [ 1, 2, 5, 1, 7, 2, 4, 2 ]
print()
print('removed by hash: ')
remove_by_hasmap(arr)

# Remove repeated digits in a given number
def removeRecur(n):
    prev_digit = n % 10
    res = prev_digit
    pow = 10
    while n:
        curr_digit = n % 10
        if curr_digit != prev_digit:
            res+= curr_digit * pow
            prev_digit = curr_digit
            pow = pow*10
        n = n//10

    return res
digit = 122233344455
print()
print()
print('removed repeted digit :',removeRecur(digit))

