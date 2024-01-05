a=int(input())
b=1
while a>0:
	print(a%10*b,end=' ')
	a=a//10
	b=b*10