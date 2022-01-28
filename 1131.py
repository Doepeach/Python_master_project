A,B=map(int,input().split())
C=int(input())
D=60*A+B+C
print((D//60)%24,D%60)
