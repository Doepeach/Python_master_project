a,b=0,0
while a<100:
    a+=1
    if a%3==0:
        print(a,end=' ')
        b+=1
        if b%10==0:
            print()