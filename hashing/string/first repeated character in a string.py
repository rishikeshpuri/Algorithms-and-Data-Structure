def firstRepeatedChar(str):
    h = {}
    for i in str:
        if i in h:
            return i
        else:
            h[i] = 0
    return
print(firstRepeatedChar("geeksforgeeks"))
