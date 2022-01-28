A,B,K=map(int,input().split())
r,t,p=0,0,-1
for i in range(A,B+1):
    cnt=0
    for j in range(1,i+1):
        if i%j==0:
            cnt+=1
    if cnt==2:
        r+=i
        t+=1
        if t==K:
            p=i
print(r)
print(p)
