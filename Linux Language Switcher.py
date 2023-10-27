# Linux persian languge changer
import os
os.system("setxkbmap -layout us,ir") # You can use any language's you want, for example: us,uk (United States, United Kingdom)
os.system("setxkbmap -option 'grp:alt_shift_toggle'") # This is the shortcut, You can use anything.
print ("Language set to (US, FA) - Toggle with Shift + Alt")
