N=int(input())
X=list(map(int,input().split()))
Y=list(map(int,input().split()))
X1=sorted(X)
Y1=sorted(Y)
cnt=0
for i in range(N):
    if X1[i]<=Y1[i]:
        cnt+=1
if cnt==N:
    print('YES')
else:
    print('No')