a=[6,7,5,7]
a[1]='A'
print(a,end='\n\n')

b=a
a[1]=7
print(a)
print(b)
print(a is b,end='\n\n')

b=a.copy()
a[1]='A'
print(a)
print(b)
print(a is b)