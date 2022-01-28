A,B=map(int,input().split())
k,s,t=1,0,0
for i in range(A,B+1):
    while k*k<i:
        k+=1
    if k*k==i:
        s+=i
        t+=1
        if t==1:
            min=i
if s==0:
    print(-1)
else:
    print(s)
    print(min)