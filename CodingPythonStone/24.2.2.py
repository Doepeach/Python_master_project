A,B=map(int,input().split())
s=0
for i in range(A,B+1):
    if i%10==7:
        s+=i
print(s)