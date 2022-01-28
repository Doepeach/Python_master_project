A,B=map(int,input().split())
k,r=0,0
while A!=0:
    k=10*k+A%10
    A=A//10
while B!=0:
    r=10*r+B%10
    B=B//10
if k>r:
    print(k)
else:
    print(r)