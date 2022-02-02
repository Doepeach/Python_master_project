import math

for i in range(2,11):
    cnt=0
    k=int(math.sqrt(i))
    for j in range(2,k+1):
        if i%j==0:
            cnt+=1
    if cnt==0:
        print(i)