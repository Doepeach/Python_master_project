N=int(input())
a=[]
even,odd=0,0
for _ in range(N):
    a.append(int(input()))
for i in range(N):
    if a[i]%2==0:
        even+=a[i]
    else:
        odd+=a[i]
print(even,odd,sep=' ')
