a=int(input())
a1=a//3600
a2=a%3600//60
a3=a%60
print(f'{a1:02}:{a2:02}:{a3:02}',end='')