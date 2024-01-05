a=list(map(int,input().split()))
N=a[0]
M=a[1]
if N%M==0:print(N//M,end='')
else:print(N//M+1,end='')
