a = [1, 3, 5, 7, 9, 11, 13]
for i in range(7):#複習  上面的寫法不好，不應該寫死 數字的範圍
  print('第i個數字是誰',a[i])
print("上面迴圈不好，下面的迴圈才會伸縮自如/全部都會照顧到")
N= len(a)
for i in range(N):
  print('第i個數字是誰',a[i])