A,B,C,D,E=list(map(int,input().split()))
sum=[sum(A),sum(B),sum(C),sum(D),sum(E)]
max=max(sum)
cook=sum.index(max)+1
print(cook,max)
