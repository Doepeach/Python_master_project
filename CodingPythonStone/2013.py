N=int(input())
s=0
for i in range(N+1):
    for j in range(N+1):
        if i>=j:
            s+=(i+j)
print(s)