def LCSubStr(x,y, m,n):
    LCSfff = [[0 for i in range(n+1)] for j in range(m+1)]
    result = 0
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                LCSfff[i][j] = 0
            elif x[i-1] == y[j-1]:
                LCSfff[i][j] = LCSfff[i-1][j-1]+1
                result = max(result, LCSfff[i][j])
                print(result)
            else:
                LCSfff[i][j] = 0
    return result
# x = 'OldSite:GeeksforGeeks.org'
# y = 'NewSite:GeeksQuiz.com'

x = '12345'
y = '123'

m = len(x)
n = len(y)
print(LCSubStr(x,y,m,n))