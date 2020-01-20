d = 256
def search(string, pattern, q):
    n = len(string)
    m = len(pattern)
    max = n-m+1
    i = 0
    j = 0
    p = 0
    t = 0
    h = 1
    for i in range(m-1):
        h = (h*d)%q

    for i in range(m):
        p = (d*p + ord(pattern[i]))%q
        t = (d*t + ord(string[i]))%q

    for i in range(max):
        if p == t:
            j = 0
            while j < m:
                if pattern[j] != string[j + i]:
                    break
                j += 1
            if j == m:
                print("Pattern found at index ", i)
        if i < n-m:
            t = (d*(t-ord(string[i])*h) + ord(string[i+m]))%q
            if t<0:
                t = t+q

string = "GEEKS FOR GEEKS"
patttern = "GEEK"
q = 101
search(string,patttern,q)