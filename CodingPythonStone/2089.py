S1,S2,S3=map(int,input().split()) #S1,S2,S3 값 input 받기
dice_sum=[]
for i in range(1,S1+1):
    for j in range(1,S2+1):
        for k in range(1,S3+1):
            dice_sum.append(i+j+k) #dice_sum에 주사위 합 list로 넣음
max_sum=max(dice_sum)
newlist=[0]*max_sum
for i in dice_sum:
    newlist[i-1]+=1
for k in newlist:
    if k==max(newlist):
        print(newlist.index(k)+1)
        break

