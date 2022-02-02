max,cnt=7,0
while True:
    A,B=map(int,input().split())
    if A==0 and B==0:
        break
    if max<A+B:
        cnt+=1
    if A+B>=8:
        max=A+B
print(cnt)