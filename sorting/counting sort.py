def CountingSort(A, k):
    B = [0 for el in A]
    # print(B)
    C = [0 for el in range(0, k+ 1)]
    # print(C)
    for i in range(0, k +1):
        C[i] = 0
    # print('c>>',C)
    for j in range(0, len(A)):
        C[A[j]] += 1
    # print(C)
    for i in range(1, k + 1):
        C[i] += C[i - 1]
    for j in range(len(A)-1, 0 - 1, -1):
        tmp = A[j]
        tmp2= C[tmp] -1
        B[tmp2] = tmp
        C[tmp] -= 1
    return B
A= [1,2,3,4,2,6,9]
print(CountingSort(A, 9))

# def countingSort(A, pos):
#     B = [0 for el in A]
#     c = [0 for el in range(10)]
#
#     for i in range(0, len(A)):
#         index = A[i]//pos
#         c[index % 10] +=1
#
#     for j in range(0, len(A)):
#         c[j] += c[j-1]
#
#     i = len(A)-1
#     while i>=0:
#         index = A[i]//pos
#         B[c[index % 10] -1] = A[i]
#         c[index %10] = c[index % 10] -1
#         i -= 1
#     for j in range(0, len(A)):
#         A[j] = B[j]
#
# def radixSort(A):
#     for i in range(0, len(A)):
#         for j in range(0, len(A)):
#             if A[i] > A[j]:
#                 max = A[i]
#     return max
#     pos = 1
#
#     while max/pos > 0:
#         countingSort(A,pos)
#         pos = pos *10
# A = [ 170, 45, 75, 90, 802, 24, 2, 66]
# # print(radixSort(A))