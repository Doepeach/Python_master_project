N,K=map(int,input().split())
S=N
while N>=K:
    S+=N//K
    N=N//K+N%K
print(S)
