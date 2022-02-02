N=int(input())
n=0
for i in range(1,N):
    if N%i==0:
        n+=i
if n==N:
    print('PERFECT')
elif n>N:
    print('ABUNDANT')
else:
    print('DEFICIENT')