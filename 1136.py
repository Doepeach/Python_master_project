A,B=map(int,input().split())
cnt=0
for i in range(A,B+1):
    k,r=i,0
    while i!=0:
        r=r*10+i%10
        i=i//10
    if k==r:
        cnt+=1
print(cnt)