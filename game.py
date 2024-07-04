import time
import util
import info
import time
import Bulls_and_Cows
from hashlib import sha256

def challenge():
  while 1:
    print("\n")
    ans = input("請先輸入通關密語(小寫): ")
    for i in range(6):
      print('Comparing' + (i%3+1)*'.' + '   ', end='\r')
      time.sleep(1)
    if sha256(ans.encode('utf-8')).hexdigest() != info.SHA_ans:
      util.twinkle_print('WRONG_KEY!!!')
      for i in range(3):
        print('請重新輸入' + (i%3+1)*'.' + '   ', end='\r')
        time.sleep(0.5)
      util.clear()
      continue
    else:
      print()
      util.cbc_print(info.BOSS_TEXT1)
      print("   ",end ='')
      util.cbc_print("......1A2B", 0.3)
      util.cbc_print(info.BOSS_TEXT2)
      print()
      flag = 0
      while 1:
        action = input('''
  Please select an action you want to do.
    * 1)  start to play
    * 2)  nahhh, i'm not gonna play
  Enter your option: ''')
        if int(action) == 1:
          flag = Bulls_and_Cows.play()
          if flag:
            break
        else:
          util.cbc_print(info.REDICU, 0.1)
          print()
          flag = 1
          break
    if flag:
      break
      
        
