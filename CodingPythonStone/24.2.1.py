N=int(input())
k,r=N,0
while k!=0:
    r=10*r+k%10
    k=k//10
if r==N:
    print('Palindrome Number')
else:
    print('Normal Number')