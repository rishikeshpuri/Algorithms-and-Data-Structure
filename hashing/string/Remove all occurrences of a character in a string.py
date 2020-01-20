def removeChar(s, c):
    counts = s.count(c)
    print(counts)
    s = list(s)
    print(s)
    while counts:
        s.remove(c)
        counts-=1
    s = ''.join(s)
    print(s)
s = "geeksforgeeks"
removeChar(s,'e')