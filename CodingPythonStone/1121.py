N=int(input())
X=int(input())
k=0
for i in range(N):
    A,B=map(int,input().split())
    if A-B>X or B-A>X:
        C=int(input())
        k+=C
    else:
        k+=max(A,B)
print(k)
