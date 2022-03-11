X=int(input())
N=int(input())
A=[]
for i in range(N):
    A.append(int(input()))
T=sum(A)
print(X*N-T+X)