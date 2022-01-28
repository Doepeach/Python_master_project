N=int(input())
i=2
while (2**i-1)<=N:
    cnt=0
    for j in range(1,i+1):
        if i%j==0:
            cnt+=1
    if cnt==2:
        cnt=0
        mersen=2**i-1
        for j in range(1,mersen+1):
            if mersen%j==0:
                cnt+=1
        if cnt==2:
            print(mersen)
    i+=1