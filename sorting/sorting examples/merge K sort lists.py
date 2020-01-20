# A = [1,2,3,4,5,5,7]
# #
# # a = [A[i].val for i in range(len(A))]
# # print(a)
# # x=0
# # y=[]
# # for i in range(1,len(A)+1):
# #     x = 0*x+i
# #     y.append((x))
# # print(y)

import sys
# from typing import List, Optional
# Matrix = List[List[int]]
# print(Matrix)
def merge2list(A,B):
    i=j=k=0
    c = []
    while i <len(A) and j < len(B):
        if A[i]<=B[j]:
            c[k] = A[i]
            i+=1
            k+=1
        elif A[i]> B[j]:
            c[k] =B[j]
            j+=1
            k+=1
    while i<len(A):
        c[k+1]=B[j+1]
    while j<len(B):
        c[k+1]=A[i+1]