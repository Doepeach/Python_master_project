N,K=map(int,input().split())
if N<=K:
    print(2)
elif (2*N)%K==0:
    print((2*N)//K)
elif (2*N)%K!=0:
    print((2*N)//K+1)
