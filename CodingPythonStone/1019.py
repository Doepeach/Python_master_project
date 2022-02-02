n=int(input())
odd,even=0,0
a=list(map(int,input().split()))
for i in range(n):
    if a[i]%2==0:
        even+=1
    else:
        odd+=1
print(even)
print(odd)
