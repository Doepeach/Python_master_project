N=int(input())
B=list(map(int,input().split()))
A=[]
for i in range(N):
    A.append((i+1)*B[i]-(i)*B[i-1])
for j in A:
    print(j,end=' ')
    