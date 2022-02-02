n=int(input())
a=[]
for _ in range(n):
    a.append(int(input()))
for i in range(n):
    if a[i]>=10:
        print(a[i],'*'*a[i],sep=' ')
    else:
        print(' ',a[i],' ','*'*a[i],sep='')