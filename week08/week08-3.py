a = [1, 3, 5, 7, 9, 11, 13, 15, 17]
N= len(a)
for i in range(1,N):
  print("現在檢查", a[i], a[i-1])
  if a[i] - a[i-1] != a[1] - a[0]:
    print("失敗",a[1],a[i-1])
    #return False
print('城市檢查結束')
