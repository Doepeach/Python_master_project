N=int(input())
A=list(map(int,input().split()))
B=sorted(A)
for i in A:
    print(i,end=' ')
print()
for j in B:
    print(j,end=' ')