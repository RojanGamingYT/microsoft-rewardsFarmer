import pyautogui as gui
import time
import random , string

time.sleep(1)

#print(gui.position())


number = 32 #input("Enter the Number")

for i in range(int(number)):
    stri = string.ascii_lowercase
    message = "".join(random.sample(stri, 10))
    gui.click(413,63)
    gui.typewrite(message)
    gui.press('Enter')
    time.sleep(1)
