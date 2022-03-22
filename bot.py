# pip install pyautogui
import pyautogui as pt
import time

print("____START____")
time.sleep(5)
counter = 1

for i in range(100):
    pt.write("Chola")
    time.sleep(0.05)
    pt.press("Enter")
    counter += 1
    print(counter)

print("____END____")
