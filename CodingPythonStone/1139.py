A,B,C=map(int,input().split())
k=A*B*C
a=[]
while k!=0:
    a.append(k%10)
    k=k//10
for i in range(10):
    print(a.count(i))

