def freq(str):
    s = str.split(' ')
    str2 = []
    for i in s:
        if i not in str2:
            str2.append(i)
    for i in range(len(str2)):
        print(str2[i], s.count(str2[i]))


str = "apple mango apple orange orange apple guava mango mango"

freq(str)

# --------OR----------
def freq1(str):
    s = str.split()
    unique_word = set(s)
    for i in unique_word:
        print('Frequency of ',i,'is :', s.count(i))



str = "apple mango apple orange orange apple guava mango mango"
print()
freq1(str)

# ----------OR------
def freq2(str):
    counts = dict()
    words = str.split()
    for i in words:
        if i in counts:
            counts[i]+=1
        else:
            counts[i]=1
    return counts
str = "apple mango apple orange orange apple guava mango mango"
print()
print(freq2(str))
