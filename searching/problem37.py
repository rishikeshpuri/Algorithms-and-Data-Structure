# def findMinimumInRotatedSortedArray(A):
#     mid, low, high = 0, 0, len(A) - 1
#
#     while A[low] >= A[high]:
#         if high - low<= 1:
#             return A[high], high
#         mid = (low+high) >> 1
#         if A[mid] == A[low]:
#             low+= 1
#         elif A[mid] > A[low]:
#             low= mid
#         elif A[mid] == A[high]:
#             high-= 1
#         else:
#             high = mid
#     return A[low], low
# A= [15, 16, 19, 20, 25, 1, 3, 4 , 5, 7, 10, 14]
# print(findMinimumInRotatedSortedArray(A))

# def binarySearch(n, k):
#     low = 0
#     high = len(n)-1
#
#     while low<=high:
#         mid = (low + high) // 2
#         if n[mid]< 1:
#             return ('input error')
#         elif n[mid]<k:
#             low = mid+1
#         elif n[mid] > k:
#             high= mid-1
#         else:
#             return mid
# a=[1,2,3,4,5,6,7,8,9,10]
# print(binarySearch(a,1))
#
# def indexOfFirstOne(arr, low, high) :
#
#     while low<=high:
#         mid = (low+high)//2
#         if arr[mid] == 1 and (mid == 0 or arr[mid-1] == 0):
#             break
#         elif arr[mid] == 1:
#             high = mid-1
#         else:
#             low = mid+1
#     return mid
#
# def posOfFirstOne(arr) :
#     l=0
#     h=1
#
#     while arr[h] == 0:
#         l = h
#         h = 2*h
#     return indexOfFirstOne(arr, l, h)
#
# arr = [ 0, 0,0,0,0,0,0,0, 1, 1, 1, 1 ]
# print( "Index = ", posOfFirstOne(arr))

def indexOfFirstZero(arr, low, high) :

    while low<=high:
        mid = (low+high)//2
        if arr[mid] == 0 and (mid == 1 or arr[mid-1] == 1):
            break
        elif arr[mid] == 0:
            high = mid-1
        else:
            low = mid+1
    return mid

def posOfFirstZero(arr) :
    l=0
    h=1

    while arr[h] == 1:
        l = h
        h = 2*h
    return indexOfFirstZero(arr, l, h)

arr = [1, 1, 1, 1,1, 0,0,0,0,0,0,0 ]
# arr = [ 0, 0,0,0,0,0,0,0, 1, 1, 1, 1 ]
print( "Index = ", posOfFirstZero(arr))