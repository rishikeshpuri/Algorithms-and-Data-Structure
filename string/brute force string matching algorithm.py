def brute_force_string_matching(string, pattern):
    ls = len(string)
    lp = len(pattern)
    max = ls-lp+1
    for i in range(max):
        j = 0
        while j < lp:
            if pattern[j] != string[j+i-1]:
                break
            j+=1

        if j == lp:
            print("Pattern found at index ", i)



string = "1234412355123661237712388"
pattern = "123"
brute_force_string_matching(string, pattern)
