import pyautogui
import webbrowser as wb
import time
wb.open("https://web.whatsapp.com/")
time.sleep(20)

for i in range(50):
    pyautogui.press("H")
    pyautogui.press("I")
    pyautogui.press("enter")