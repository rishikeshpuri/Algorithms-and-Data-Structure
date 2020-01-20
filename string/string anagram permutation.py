max = 256

def compare(arr1, arr2):
    for i in range(max):
        if arr1[i] != arr2[i]:
            return False
    return True

def search(txt, patt):
    m = len(patt)
    n = len(txt)

    countP = [0]*max
    countTxt = [0]*max
    for i in range(m):
        countP[ord(patt[i])] +=1
        countTxt[ord(txt[i])] +=1

    for i in range(m, n):
        if compare(countP, countTxt):
            print("Found at index :", (i-m))

        countTxt[ord(txt[i])] +=1
        countTxt[ord(txt[i-m])] -=1

    if compare(countP, countTxt):
        print("Found at index :", (n-m))

txt = "BACDGABCDA"
pat = "ABCD"
search(txt, pat)