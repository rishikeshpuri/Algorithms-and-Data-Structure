NO_OF_CHAR = 256

def toList(string):
    temp = []
    for i in string:
        temp.append(i)
    return temp

def toString(list):
    return ''.join(list)

def getCharCountArray(string):
    count = [0]*NO_OF_CHAR
    for i in string:
        count[ord(i)] +=1
    return count

print(toList('abcccccda'))
print(toString(['a', 'b', 'c', 'c', 'c', 'c', 'c', 'd', 'a']))
print(getCharCountArray('abcccccda'))

def removeDirtyChar(string, mask_string):
    count = getCharCountArray(mask_string)
    ip_ind = 0
    res_ind = 0
    str_list = toList(string)
    while ip_ind !=len(str_list):
        temp = str_list[ip_ind]
        if count[ord(temp)] == 0:
            str_list[res_ind] = str_list[ip_ind]
            res_ind+=1
        ip_ind+=1
    return toString(str_list[0:res_ind])

mask_string = "mask"
string = "geeksforgeeks"
print(removeDirtyChar(string, mask_string))