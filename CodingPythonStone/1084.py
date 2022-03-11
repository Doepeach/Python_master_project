A=list(map(int,input().split()))
B=A[:-1]
cnt=0
for i in B:
    if (2*i) in B:
        cnt+=1
print(cnt)

        
