N=int(input())
cnt=0
for i in range(1,501):
    for k in range(1,i):
        if (i**2)-(k**2)==N:
            cnt+=1
print(cnt)