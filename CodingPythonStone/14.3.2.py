A,B=map(int,input().split())
if A==1 and B==1:
    print('both')
elif A==1 or B==1:
    print('either')
else:
    print('neither')