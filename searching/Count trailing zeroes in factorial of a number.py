def findTrailingZeros(n):
    # Initialize result
    count = 0

    # Keep dividing n by
    # powers of 5 and
    # update Count
    i = 5
    while (n / i >= 1):
        count += int(n / i)
        i *= 5

    return (count)

print("Count of trailing 0s is",findTrailingZeros(500))

def trailingZeroes( n ):
    cnt = 0
    while n > 0:
        n =int(n/5)
        cnt += n
    return cnt
print(trailingZeroes(1))