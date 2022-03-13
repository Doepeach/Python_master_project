N=int(input())
store=list(map(int,input().split()))
left=min(store)
right=max(store)
print(2*(right-left))

