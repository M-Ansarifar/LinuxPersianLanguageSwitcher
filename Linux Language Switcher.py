# Linux persian languge changer
import os, time

print ("Developed by Mo-Ans\n")
time.sleep(1.8)
os.system("setxkbmap -layout us,ir")
os.system("setxkbmap -option 'grp:alt_shift_toggle'")
print ("Language set to (US, FA) - Toggle with Shift + Alt")