def KMPSearch(string, pattern):
    m= len(pattern)
    n = len(string)
    lps = [0]*m
    j =0
    computeLPSArray(pattern, m, lps)
    i = 0
    while i < n:
        if pattern[j] == string[i]:
            i+=1
            j+=1
        if j == m:
            print("pattern found at index ", i-j)
            j = lps[j-1]
        elif i < n and pattern[j] !=string[i]:
            if j!=0:
                j = lps[j-1]
            else:
                i+=1


def computeLPSArray(pattern, m, lps):
    len = 0
    # lps[0]
    i = 1
    while i < m:
        if pattern[i] == pattern[len]:
            len+=1
            i+=1
        else:
            if len!=0:
                len = lps[len-1]
            else:
                lps[i] = 0
                i+=1
string = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
KMPSearch(string, pattern)