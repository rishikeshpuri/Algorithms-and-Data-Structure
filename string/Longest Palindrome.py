s = "was it a cat I saw?"
# Solution uses extra space proportional to sixe of string-'s'

x = ''.join([i for i in s if i.isalnum()]).replace(" ", "").lower()
print(x == x[::-1])

# -----------OR------------
def is_palindrome(str):
    i = 0
    j = len(str)-1
    while i < j:
        while not str[i].isalnum() and i < j:
            i+=1
        while not str[j].isalnum() and i < j:
            j-=1

        if str[i].lower() != str[j].lower():
            return False
        i+=1
        j-=1
    return True

print(is_palindrome(s))