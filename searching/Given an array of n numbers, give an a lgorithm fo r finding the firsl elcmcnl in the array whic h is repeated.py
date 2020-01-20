# Given an array of n numbers, give an algorithm for
# finding the first element in the array which is repeated.
# For example, in the array A = (3, 2, 1, 2, 2, 3}, the first repeated number is 3 (not 2).
# That means, we need to return lhe first element among the repeated elements.


def firstDuplicate(n):

    for i in range(0,len(n)):
        count=0
        max = 0
        for j in range(i+1, len(n)):
            if n[i] == n[j]:
                count+=1
        if max < count:
            element = n[i]
            print(element)
            break









A = [3, 2, 1, 2,2,2,1,3]
firstDuplicate(A)
