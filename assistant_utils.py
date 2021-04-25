

import pyautogui

#screen_shot(file_name)
def screen_shot(file_name):
    screenshot = pyautogui.screenshot()
    file_name = file_name + ".png"
    screenshot.save(file_name)
    print("file saved here: " + file_name)
    #screen_shot("test_fil")
