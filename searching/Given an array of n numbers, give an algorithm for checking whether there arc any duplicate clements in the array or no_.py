"""
Given an array of n numbers, give an algorithm for checking whether
there are any duplicate elements in the array or no?
"""

# def checkDuplicateNumbers(n):
#     for i in range(0, len(n)):
#         for j in range((0),len(n)):
#             if n[i] == n[j] and i!=j:
#                 print('Duplicate exist:',n[i])
#                 return
#     print('no Duplicate exist')
#
# A = [13,2, 10,20,22,32]
# checkDuplicateNumbers(A)
# A = [3,2, 1,2,3]
# checkDuplicateNumbers(A)
# #
#
# def CheckDuplicatesSorting(A):
#     A.sort()
#     for i in range(0,len(A)):
#         for j in range(i+ 1 ,len(A)):
#             if(A[i] == A[i+1]):
#                 print("Duplicates exist:", A[i])
#                 return
#     print("No duplicates in given array.")
#
# A=[133,2, 10,20,22,32]
# CheckDuplicatesSorting(A)
#
# A=[3,2,1,1,2,3]
# CheckDuplicatesSorting(A)
import math
# def CheckDuplicatesNegationTechnique(A):
#     A.sort()
#     for i in range(0,len(A)):
#         if(A[abs(A[i])] < 0):
#             print("duplicates exist:", A[i])
#             return
#         else:
#             A[A[i]]= - A[A[i]]
#     print("No duplicates in given array.")
# A= [3,2, 1,2,2,3]
# CheckDuplicatesNegationTechnique(A)

# a=[1,2,3]
# x=a[1]
# y=a[a[1]]
# print(x)
# print(y)
