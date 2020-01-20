def PrintTwoRepeatedElementsBruteForce(n):
    for i in range(0, len(n)):
        for j in range(i+1,len(n)):
            if n[i] == n[j] and i!=j:
                print(n[i])
A= [3,5,7,4,2,4,2,1,9]
PrintTwoRepeatedElementsBruteForce(A)

