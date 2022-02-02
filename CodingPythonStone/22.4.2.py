A=int(input())
S,T=10000,0
while S>=A:
    S-=A
    print(S)
    T+=1
print(T)