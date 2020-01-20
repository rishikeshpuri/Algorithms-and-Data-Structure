# Given an array of n numbers. Give an a lgorithm for finding the
# element which appears the max number of times in the array?

# A = [13,2, 10,20,22,32]
# checkDuplicateNumbers(A)
# A = [3,2,1,2,2,3,2,1,3]
# checkDuplicateNumbers(A)

# def MaxRepititionsBruteForcc(A):
#     n = len(A)
#     count = max =0
#     for i in range(0,n):
#         count = 1
#         for j in range(0,n):
#             if( i != j and A[i] == A[j]):
#                 count+= 1
#         if max< count:
#             max= count
#             maxRepeatedElement = A[i]
#
#     print (maxRepeatedElement, "repeated for", max)
# A= [3,2,1,2,2,3,2,1,3,1,5,5,5,5]
# MaxRepititionsBruteForcc(A)

# def MaxRepititionsWithSort(A):
#     A.sort()
#     print (A)
#
#     count = max = 1
#     element = A[0]
#     for i in range(1,len(A)):
#         if (A[i] == element):
#             count+= 1
#             if count > max:
#                 max= count
#                 maxRepeatedElement = element
#         else:
#                 count= 1
#                 element= A[i]
#     print(maxRepeatedElement, "repeated for", max)
#
# A = [3,2, 1,3,2,3,2,3,3]
# MaxRepititionsWithSort(A)

def MaxRepititionsEfficicnt(A):
    print(A)
    n = len(A)
    print(n)
    max = 0
    for i in range(0,len(A)):
        A[A[i]%n] += n
    print(A)
    for i in range(0,len(A)):
        if(A[i]/n > max):
            max = A[i]/n
            maxIndex =i
    print(maxIndex, "repeated for", max, " times")

A = [3,2,2,3,2,2,2,3,3]
MaxRepititionsEfficicnt(A)
