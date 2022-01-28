N=int(input())
s,t=0,0
for i in range(1,N+1):
    if i%2==0:
        s+=i
    else:
        t+=i
print(s)
print(t)
