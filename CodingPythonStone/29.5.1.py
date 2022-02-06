from re import S


a=tuple(range(1,100,2))
s=0
for i in range(50):
    s+=a[i]
print(s)