a=[0]
for _ in range(10):
    a.append(int(input()))
s=0
for x in a[1:]:
    s+=x
    if s<=100:
        res=s
    else:
        if 100-res>s-100:
            res=s
        break
print(res)