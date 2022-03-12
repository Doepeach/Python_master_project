N=int(input())
X=list(map(int,input().split()))
M=int(input())
for i in range(M):
    k,a,b=map(int,input().split())
    if k==1:
        print(min(X[a-1:b]))
    elif k==2:
        print(max(X[a-1:b]))
    elif k==3:
        print(sum(X[a-1:b]))
