import pyautogui
import keyboard
import time
import csv
import mouse

time.sleep(4)

Url = ''
phone_num = []
num = 0

with open("students_no.csv", "r") as f:
    line = csv.reader(f)

    for i in line:
        phone_num.append(i)



while num < len(phone_num[0]):
    #whatsapp search bar (273,264)
    pyautogui.click(282, 280)


    keyboard.press("ctrl")
    keyboard.press("a")
    time.sleep(0.3)
    keyboard.release("ctrl")
    keyboard.press("backspace")

    time.sleep(0.5)
    #write the phone number
    keyboard.write(phone_num[0][num])

    time.sleep(0.8)
    #contact list (308, 430)
    pyautogui.click(308, 430)

    time.sleep(0.3)
    #type the URL of the invite in chat (861,957)
    pyautogui.click(861,957)

    
    keyboard.press("ctrl")
    keyboard.press("v")
    time.sleep(0.5)

    # for i in range(250):
    #     keyboard.write(Url)
    #     time.sleep(0.05)
    #     keyboard.press("enter")

    #Send invite (1838,930)
    pyautogui.click(1838, 930)

    #keyboard.press("enter")
    num += 1
    time.sleep(0.5)
    