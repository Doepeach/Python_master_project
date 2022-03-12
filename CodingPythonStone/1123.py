N=int(input())
Everycard=[2,3,4,5,6,7,8,9,10,11,11,11,11]*4
Card=[]
large=0
small=0
for _ in range(N):
    Card.append(int(input()))
Sumcard=sum(Card)
X=21-Sumcard
for i in Everycard:
    if i>X:
        large+=1
    else:
        small+=1
if large>small:
    print('STOP')
else:
    print('DRAW')