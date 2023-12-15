a=list(map(int,input('Enter the number of values to be processed: ').split()))
N=len(a)
ans =1
for i in range(1,N):
	print('Enter a value: ',end='')
	ans*=a[i]
print('Product of the',a[0],'values is',ans,end='')