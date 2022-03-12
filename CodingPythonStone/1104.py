P,Q=map(int,input().split())
p=[]
q=[]
for i in range(1,P+1):
    if P%i==0:
        p.append(i)
for j in range(1,Q+1):
    if Q%j==0:
        q.append(j)
for i in p:
    for j in q:
        print(i,j)