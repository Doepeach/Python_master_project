N=int(input())
s=1
print(N,end='!=(')
for i in range(1,N):
    print(i,end='*')
    s*=i
print(N,end=')=')
print(s*N)
