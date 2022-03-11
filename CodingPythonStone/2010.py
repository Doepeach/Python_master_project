N=int(input())
A=list(map(int,input().split()))
X=(sum(A)//N)
s=0
for i in A:
    if i>X:
        s+=i-X
print(s)