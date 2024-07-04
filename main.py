import util
import info
import game

def main():
  util.clear()
  print()
  print("---------------------------------------  歡迎來到  ---------------------------------------")
  print(info.WELCOME_TEXT)
  util.cbc_print("這站是 SITCON HACKATHON 2024 final stage\n", 0.1)
  util.cbc_print("Press enter to continue...\n", 0.1)
  input()
  util.clear()
  game.challenge()

if __name__ == '__main__':
    main()