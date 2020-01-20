s = "i like this program very much"
words = s.split(' ')
string = []
for word in words:
    string.insert(0, word)

print("Reversed String:")
print(" ".join(string))
print()
def reverse(str):
    s = str.split()
    l =[]
    for i in s:
        l.append(i)
    return l[::-1]
s = 'my name is rishi'
print(reverse(s))
print()

def tostr(list):
    x = reverse(list)
    for i in x:
        print(i, end=' ')
tostr('my 123')

# -------or-------
def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start+=1
        end-=1
A = [1, 2, 3, 4, 5, 6]
print()
print()
print(A)
reverseList(A, 0, 5)
print("Reversed list is")
print(A)

# ---------by recursive-----
def recur_reverseList(A, start, end):
    if start < end:
        return
    A[start], A[end] = A[end], A[start]
    recur_reverseList(A, start+1, end-1)

A = [1, 2, 3, 4, 5, 6]
print()
print(A)
recur_reverseList(A, 0, 5)
print("Reversed list is by recursive : ")
print(A)