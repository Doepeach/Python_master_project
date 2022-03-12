N=int(input())
x=int(input())
son=list(map(int,input().split()))
it=0
if x%2==1:
    for i in son:
        if i>0:
            it+=i**x
else:
    for i in son:
        it+=i**x
print(it)