r=0
for i in range(1,101):
    cnt=0
    for j in range(1,i+1):
        if i%j==0:
            cnt+=1
    if cnt==2:
        print(i,end=' ')
        r+=1
        if r%5==0:
            print()