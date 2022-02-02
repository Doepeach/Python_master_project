a=[5,7,13,11,6,10,45,11,4,9]
cnt=0
for i in range(10):
    if a[i]%2==0:
        cnt+=a[i]
print(cnt)