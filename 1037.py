A,B,C,D=map(int,input().split())
a,b,c,d=map(int,input().split())
S=A+B+C+D
T=a+b+c+d
if S>=T:
    print(S)
else:
    print(T)
    