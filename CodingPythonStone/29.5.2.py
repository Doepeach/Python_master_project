a=tuple(range(1,100,2))
t=0
for i in range(50):
    s=0
    for j in range(1,a[i]+1):
        if a[i]%j==0:
            s+=1
    if s%2!=0:
        t+=a[i]
print(t)