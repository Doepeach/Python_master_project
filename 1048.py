N=int(input())
S,k=N,0
while S!=0:
    k=k*10+S%10
    S=S//10
print(N+k)