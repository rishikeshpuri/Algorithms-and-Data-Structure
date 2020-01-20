# def findMissingNumber(n):
#
#     for i in range(1,len(n)+1):
#         found = 0
#         for j in range(0,len(n)):
#             if i == n[j]:
#                 found = 1
#
#         if found == 0:
#             print('missing number:',i )
# A= [8,2,1,4,6,5,7,9,0]
# findMissingNumber(A)
#
# def sortFindMissingNumber(n):
#     n.sort()
#     print(n)
#
#     for i in range(1,len(n)):
#         found = 0
#         for j in range(0,len(n)):
#             if i == n[j]:
#                 found = 1
#
#         if found == 0:
#             print('missing number:',i )
#
#
# A= [8,2,1,4,5,7,9]
# sortFindMissingNumber(A)

def sortFindMissingNumber(number):
    number.sort()
    print(number)

    l = number[-1]
    print("Last digit of series : ", l)

    # sum = (n * (n + 1)/ 2)
    # print(sum)

    for i in range(1, l+1):
        sum = i*(i+1)//2
    print("Total sum of series : ", sum)

    for j in range(0, len(number)):

        sum = sum - number[j]
    print("Number missing in series : ",sum)



A = [2, 1, 4,]
sortFindMissingNumber(A)