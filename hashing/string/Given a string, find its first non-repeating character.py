No_OF_CHAR = 256

def getCharCountArray(string):
    counts = [0]*No_OF_CHAR
    for i in string:
        counts[ord(i)] +=1
    return counts

def firstNonRepeatingChar(string):
    count = getCharCountArray(string)
    index = -1
    k = 0
    for i in string:
        if count[ord(i)] == 1:
            index = k
            break
        k+=1
    return index
string = "geeksforgeeks"
index = firstNonRepeatingChar(string)
# if index==1:
#     print("Either all characters are repeating or string is empty")
# else:
#
#     print("First non-repeating character is " + string[index])

print(string[firstNonRepeatingChar(string)])