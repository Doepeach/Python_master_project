A=[1,2,3,4,5,6,7,8,9,10]
for i in range(9):
    for j in range(i+1,10):
        if A[i]<A[j]:
            A[i],A[j]=A[j],A[i]
print(A)