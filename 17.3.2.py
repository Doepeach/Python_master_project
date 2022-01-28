A,B=map(int,input().split())
s=0
for i in range(A,B+1):
    if i%5==0:
        s+=i
print(s)