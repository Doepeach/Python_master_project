N=int(input())
day,gold,s=0,0,0
while day<N:
    gold+=1
    day+=gold
    s+=gold*gold
s-=(day-N)*gold
print(s)