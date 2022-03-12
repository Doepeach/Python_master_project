N=int(input())
a=[]
for i in range(N):
    a.append(int(input()))
b=[0]*(max(a)+1)
for x in a:
    b[x]+=1
maxv=max(b)
idx=b.index(maxv)
print(idx)