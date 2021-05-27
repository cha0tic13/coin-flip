import random
import win32con
import win32gui
import os
import time

# ||| ############################# |||
# ||| Coin-Fliper whatever dunno.   |||
# ||| Version 1.0.1.                |||
# ||| Made by n1ubdev, in Python3.  |||
# ||| ############################# |||


# Sets the window position to the top left corner.
hwnd = win32gui.GetForegroundWindow()
win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,0,0,500,200,0)

version = "1.0.1"

# Heads or Tails
torh = [
  "heads",
  "tails"
]

# "flip" function.
def flip():
    print("\n[\u001b[31mi\u001b[37m] You bet on "+ option +". ")
    print("[\u001b[31m!\u001b[37m] Flipping the coin...")
    time.sleep(1)
    result = random.choice(torh)
    if option == result:
        print("[\u001b[31m!\u001b[37m] It landed on "+ result + "! You won!!")
    else:
        print("[\u001b[31m!\u001b[37m] It landed on "+ result + ". You lost.")

# The program itself.
if __name__ == "__main__":
    os.system('cls & title [Coin flip] made in Python')
    print(
        '\n[\u001b[31m+\u001b[37m] Bet on Tails by typing "T" or "tails"',
        '\n[\u001b[31m+\u001b[37m] Bet on Heads by typing "H" or "heads"',
        '\n[\u001b[31m+\u001b[37m] Current version is '+ version
    )

    option = input('\n\u001b[31mHeads or Tails >\u001b[37m ')

    # heads
    if "heads" in option:
        flip()
    
    if "H" in option:
        option = "heads"
        flip()
    
    if "h" in option:
        option = "heads"
        flip()

    # tails
    if "tails" in option:
        option = "tails"
        flip()

    if "T" in option:
        option = "tails"
        flip()
    
    if "t" in option:
        option = "tails"
        flip()

    elif "exit" in option:
        print("[\u001b[31mX\u001b[37m] Exiting...")
        exit()

    else: 
        print("[\u001b[31m!\u001b[37m] An error occurred.")
        print("[\u001b[31mi\u001b[37m] Might just be a typo.")
        time.sleep(0.5)
        print("[\u001b[31mX\u001b[37m] Exiting...")
        exit() 
