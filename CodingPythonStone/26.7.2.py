max=0
while True:
    A,B=map(int,input().split())
    if A==0 and B==0:
        break
    if max<A+B:
        max=A+B
print(max)