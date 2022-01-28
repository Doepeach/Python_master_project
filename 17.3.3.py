N=int(input())
s=0
for i in range(1,N+1):
    if N%i==0:
        s+=1    
print(s)