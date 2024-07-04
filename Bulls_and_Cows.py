import util
import time
import random
import cool
import info

def play():
  util.clear()
  util.cbc_print("\nLet's get started\n")
  for i in range(4):
    print('出題中' + (i%4+1)*'.' + '   ', end='\r')
    time.sleep(1)
  ans = []
  i = 1
  while i<=4:
    tmp = random.randint(0, 9)
    flag = 1
    for num in ans:
      if tmp == num:
        flag = 0
        break
    if flag:
        ans.append(tmp)
        i+=1
  print("放馬過來吧，區區coder，不足為奇")
  count = 0
  zzz = 0
  while count<7:
    if count == 6:
      print("剩最後一次囉，我可不會同情你的歐\n")
    arr = input("請猜4個數字（各為0~9, 數字間不能重複, 數字間也不用有間隔） : ")
    your_ans = []
    for chr in arr:
      your_ans.append(int(chr))
    a = 0
    b = 0
    for num1 in range(4):
      for num2 in range(4):
        if ans[num1] == your_ans[num2] and num1 == num2:
          a+=1
          break
        elif ans[num1] == your_ans[num2]:
          b+=1
          break
    if a == 4:
      zzz = 1
      break
    util.cbc_print(f"你得到 {a}A{b}B\n")
    count+=1
  if zzz:
    util.cbc_print(f"{info.NO}")
    cool.main()
    return 1
  else:
    util.cbc_print(f"{info.YES}")
    return 0
    