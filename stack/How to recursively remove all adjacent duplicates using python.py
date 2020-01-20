def removeUtil(string, last_removed):
    if len(string) == 0 or len(string) == 1:
        return string

    if string[0] == string[1]:
        last_removed = ord(string[0])
        while len(string) > 1 and string[0] == string[1]:
            string = string[1:]
        string = string[1:]
        return removeUtil(string, last_removed)

    rem_str = removeUtil(string[1:], last_removed)

    if len(rem_str) != 0 and rem_str[0] == string[0]:
        last_removed = ord(string[0])
        return rem_str[1:]

    if len(rem_str) == 0 and last_removed == ord(string[0]):
        return rem_str
    return [string[0]] + rem_str

def remove(string):
    last_removed = 0
    return toStrring(removeUtil(toList(string), last_removed))


def toList(string):
    x= []
    for i in string:
        x.append(i)
    return x

def toStrring(x):
    return ''.join(x)
string1 = "geeksforgeeg"

print(remove(string1))
a = '6241212219'
print(remove(a))
# by using STACK

def removeAdjacentDuplicutes(str):
    stkptr = -1
    i= 0
    size =len(str)
    while i<size:
        if (stkptr == -1 or str[stkptr]!=str[i]):
            stkptr += 1
            str[stkptr] = str[i]
            i+=1
        if i < size and str[stkptr]==str[i]:
            while i < size and str[stkptr]==str[i]:
                i += 1
            stkptr -= 1
        # else:
        #     while i < size and str[stkptr]==str[i]:
        #         i += 1
        #     stkptr -= 1
    stkptr+=1
    str = str[0:stkptr]
    print(str)
removeAdjacentDuplicutes(['6', '2', '4', '1', '2', '1', '2', '2', '1', '9'])
