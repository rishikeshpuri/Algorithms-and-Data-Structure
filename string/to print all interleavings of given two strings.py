def toString(list):
    return ''.join(list)

def printILsRecursive(str1, str2, istr, m, n, i):
    if m==0 and n==0:
        print(toString(istr))

    if m !=0:
        istr[i] = str1[0]
        printILsRecursive(str1[1:], str2, istr, m-1, n, i+1)

    if n != 0:
        istr[i] = str2[0]
        printILsRecursive(str1, str2[1:], istr, m, n-1, i + 1)

def printILs(str1, str2, m, n):
    istr = ['']*(m+n)
    printILsRecursive(str1,str2, istr, m, n, 0)

str1 = "AB"
str2 = "CD"
printILs(str1, str2, len(str1), len(str2))