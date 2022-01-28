N=int(input())
s=0
for i in range(1,N+1):
    if i%2==1:
        s+=i**2
    else:
        s-=i**2
print(s)
