A,B=map(int,input().split())
cnt=0
A_list=list(map(int,str(A)))
B_list=list(map(int,str(B)))
for i in A_list:
    for j in B_list:
        cnt+=i*j
print(cnt)

