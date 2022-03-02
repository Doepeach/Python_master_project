str='Euler'
a=[1,2,3,4,5,6,7,8,9,10]
r=range(10)
print(len(str))
print(len(a))
print(len(r))

del a[0]
print(a)
del a[::2]
print(a)

del str
del a
del r