cnt=0
for i in range(1,101):
    if i%2==0:
        print(i,end=' ')
        cnt+=i
    if cnt>50:
        break
print()
print(cnt)