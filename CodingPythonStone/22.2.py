a,cnt=0,0
while a<100:
    a+=1
    if a%2==1:
        print(a,end=' ')
        cnt+=1
        if cnt%5==0:
            print()