sum,num=0,28
for i in range(1,num):
    if num%i==0:
        sum+=i
if num==sum:
    print('Perfect Number')