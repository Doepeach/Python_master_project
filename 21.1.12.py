for i in range(1,6):
    print(' '*(5-i),end='')
    for j in range(i,3*i-1):
        print(chr(64+j),end='')
    print()