def toList(string):
    temp = []
    for i in string:
        temp.append(i)
    return temp

def toString(list):
    return ''.join(list)

def stringFilter(string):
    n = len(string)

    i = -1
    j = 0
    while j < n:
        if j< n-1 and string[j] == 'a' and string[j+1] == 'c':
            j += 2
        elif string[j] == 'b':
            j +=1
        elif i >=0 and string[j] == 'c' and string[i] == 'a':
            i -= 1
            j +=1
        else:
            i+=1
            string[i] = string[j]
            j+=1
    i+=1
    return toString(string[:i])
string1 = "ad"
print(stringFilter(toList(string1)))
string2 = "acbac"
print(stringFilter(toList(string2)))
string3 = "aaac"
print(stringFilter(toList(string3)))
string4 = "react"
print(stringFilter(toList(string4)))
string5 = "ababaac"
print(stringFilter(toList(string5)))
