import random
import win32con
import win32gui
import os
import time

# Sets the window position to the top left corner.
hwnd = win32gui.GetForegroundWindow()
win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,0,0,500,200,0)

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
        '\n[\u001b[31m+\u001b[37m] Bet on Tails by typing "tails"',
        '\n[\u001b[31m+\u001b[37m] Bet on Heads by typing "heads"',
        '\n[\u001b[31m!\u001b[37m] Making improvements later.'
    )

    option = input('\n\u001b[31mHeads or Tails >\u001b[37m ')

    if "heads" in option:
        flip()

    elif "tails" in option:
        flip()

    else: 
        print("[\u001b[31m!\u001b[37m] An error occurred.")
        print("[\u001b[31mi\u001b[37m] Might just be a typo.")
        print("[\u001b[31mX\u001b[37m] Exiting...")
        exit()

        


