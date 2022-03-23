# pip install pyautogui
import pyautogui as pt
import time

print("____START____")
print("Now open Whatsapp web and Click on person to send message")
time.sleep(30)
msg = input("Enter Your message :- ")
run = int(input("Enter How many times you want to message :- "))
counter = 1
print("Now Open Whatsapp Web And Not change The screen")
time.sleep(5)
print("Now Just Sit Back")
for i in range(run):
    pt.write(msg)
    time.sleep(0.05)
    pt.press("Enter")
    counter += 1
    print(counter)

print("____END____")
