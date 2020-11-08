import cv2
import pyautogui
from PIL import ImageGrab
import threading
import time
stop = 0
flag2 = True
flag3 = True
calcP = 0
changeP = 0

def loot():
    if stop > 0:
        if changeP == 1:
            change()
            time.sleep(0.5)
            loot()
             # global stop, changeP
             # changeP = 0
             # stop = 0
        else:
            time.sleep(0.5)
            loot()

    else:
         while flag2:
             shipX = 1394 #+-225
             shipY = 490  #130
             pyautogui.click(x=shipX, y=shipY -128)
             screen_take = ImageGrab.grab(bbox=(1155, 280, 1660, 680))
             screen_take.save('/Users/admin/Pictures/testpil/screen_take2.png')
             screen_takeO = cv2.imread('/Users/admin/Pictures/testpil/screen_take2.png')
             take = cv2.imread('/Users/admin/Pictures/testpil/take.png')
             result = cv2.matchTemplate(screen_takeO, take, cv2.TM_CCOEFF_NORMED)
             (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
             pyautogui.click(x=maxloc[0] + 1160, y=maxloc[1] + 280)
             time.sleep(0.5)

             pyautogui.click(x=shipX + 130, y=shipY)
             screen_take = ImageGrab.grab(bbox=(1155, 280, 1660, 680))
             screen_take.save('/Users/admin/Pictures/testpil/screen_take2.png')
             screen_takeO = cv2.imread('/Users/admin/Pictures/testpil/screen_take2.png')
             take = cv2.imread('/Users/admin/Pictures/testpil/take.png')
             result = cv2.matchTemplate(screen_takeO, take, cv2.TM_CCOEFF_NORMED)
             (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
             pyautogui.click(x=maxloc[0] + 1160, y=maxloc[1] + 280)
             time.sleep(0.5)

             pyautogui.click(x=shipX - 130, y=shipY)
             screen_take = ImageGrab.grab(bbox=(1155, 280, 1660, 680))
             screen_take.save('/Users/admin/Pictures/testpil/screen_take2.png')
             screen_takeO = cv2.imread('/Users/admin/Pictures/testpil/screen_take2.png')
             take = cv2.imread('/Users/admin/Pictures/testpil/take.png')
             result = cv2.matchTemplate(screen_takeO, take, cv2.TM_CCOEFF_NORMED)
             (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
             pyautogui.click(x=maxloc[0] + 1160, y=maxloc[1] + 280)
             time.sleep(0.5)

             pyautogui.click(x=shipX, y=shipY+128)
             screen_take = ImageGrab.grab(bbox=(1155, 280, 1660, 680))
             screen_take.save('/Users/admin/Pictures/testpil/screen_take2.png')
             screen_takeO = cv2.imread('/Users/admin/Pictures/testpil/screen_take2.png')
             take = cv2.imread('/Users/admin/Pictures/testpil/take.png')
             result = cv2.matchTemplate(screen_takeO, take, cv2.TM_CCOEFF_NORMED)
             (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
             pyautogui.click(x=maxloc[0] + 1160, y=maxloc[1] + 280)
             time.sleep(0.5)
             loot()

def kill():

    if stop > 0:
        time.sleep(0.3)
        kill()
    else:
        while flag2:
            time.sleep(0.1)
            pyautogui.keyDown('capslock')
            pyautogui.keyUp('capslock')
            kill()

def change():
    global calcP
    calcP = 0
    # Поиск "Доки"
    time.sleep(2)
    screen_panel = ImageGrab.grab(bbox=(1790, 220, 1915, 550))
    screen_panel.save('/Users/admin/Pictures/testpil/screen_panel.png')
    screen_panel = cv2.imread('/Users/admin/Pictures/testpil/screen_panel.png')
    screen_doki = cv2.imread('/Users/admin/Pictures/testpil/Doki.png')

    result = cv2.matchTemplate(screen_panel, screen_doki, cv2.TM_CCOEFF_NORMED)
    (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
    pyautogui.click(x=maxloc[0] + 1790 + 5, y=maxloc[1] + 220 + 5)

    time.sleep(1)
    # Поиск "Корабль"
    screen_info = ImageGrab.grab(bbox=(900, 200, 1860, 750))
    screen_info.save('/Users/admin/Pictures/testpil/screen_info.png')
    screen_info = cv2.imread('/Users/admin/Pictures/testpil/screen_info.png')
    screen_button = cv2.imread('/Users/admin/Pictures/testpil/button1.png')

    result = cv2.matchTemplate(screen_info, screen_button, cv2.TM_CCOEFF_NORMED)
    (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)

    pyautogui.click(x=maxloc[0] + 900, y=maxloc[1] + 200)

    time.sleep(1)
    # Поиск "Снаряжение"
    screen_info = ImageGrab.grab(bbox=(900, 200, 1860, 750))
    screen_info.save('/Users/admin/Pictures/testpil/screen_info.png')
    screen_info = cv2.imread('/Users/admin/Pictures/testpil/screen_info.png')
    screen_button = cv2.imread('/Users/admin/Pictures/testpil/button2.png')

    result = cv2.matchTemplate(screen_info, screen_button, cv2.TM_CCOEFF_NORMED)
    (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)

    pyautogui.click(x=maxloc[0] + 900, y=maxloc[1] + 200)

    time.sleep(1)
    # Поиск новой пилы
    screen_info = ImageGrab.grab(bbox=(900, 200, 1860, 750))
    screen_info.save('/Users/admin/Pictures/testpil/screen_info.png')
    screen_info = cv2.imread('/Users/admin/Pictures/testpil/screen_info.png')
    screen_button = cv2.imread('/Users/admin/Pictures/testpil/new_saw.png')

    result = cv2.matchTemplate(screen_info, screen_button, cv2.TM_CCOEFF_NORMED)
    (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)

    pyautogui.moveTo(maxloc[0] + 900, maxloc[1] + 200)
    pyautogui.dragTo(1590, 440, button='left')

    time.sleep(1)
    # Поиск крестика
    screen_info = ImageGrab.grab(bbox=(900, 200, 1860, 750))
    screen_info.save('/Users/admin/Pictures/testpil/screen_info.png')
    screen_info = cv2.imread('/Users/admin/Pictures/testpil/screen_info.png')
    screen_button = cv2.imread('/Users/admin/Pictures/testpil/close.png')

    result2 = cv2.matchTemplate(screen_info, screen_button, cv2.TM_CCOEFF_NORMED)
    (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result2)

    pyautogui.click(x=maxloc[0] + 900 + 3, y=maxloc[1] + 200 + 3)
    time.sleep(1)


def calc():
    global stop
    global calcP
    global changeP
    if stop == 0:
        while flag3:

            if calcP < 200:
                stop = 0
                calcP += 1
                screen_saw_panel = ImageGrab.grab(bbox=(1100, 950, 1750, 1150))
                screen_saw_panel.save('/Users/admin/Pictures/testpil/screen_saw_panel.png')
                screen_saw_panel = cv2.imread('/Users/admin/Pictures/testpil/screen_saw_panel.png')
                screen_saw = cv2.imread('/Users/admin/Pictures/testpil/saw.png')
                result = cv2.matchTemplate(screen_saw_panel, screen_saw, cv2.TM_CCOEFF_NORMED)
                (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
                pyautogui.click(x=maxloc[0] + 1100, y=maxloc[1] + 950)
                time.sleep(10)
                calc()
            else:
                print('замена')

                changeP = 1
                stop = 1



    else:
        while flag3:
            time.sleep(5)
            calc()


t = threading.Thread(target=loot, args=())
k = threading.Thread(target=kill, args=())
c = threading.Thread(target=calc, args=())

def program():
         screen_map = ImageGrab.grab(bbox=(1700,40,1880,220))
         screen_map.save('/Users/admin/Pictures/testpil/screen_map.png')
         screen_map = cv2.imread('/Users/admin/Pictures/testpil/screen_map.png')
         map_activ = cv2.imread('/Users/admin/Pictures/testpil/pers2.png')
         color_low = (0, 140, 230)
         color_high = (40, 200, 255)
         map = cv2.inRange(screen_map, color_low, color_high)
         activ = cv2.inRange(map_activ, color_low, color_high)
         result = cv2.matchTemplate(map, activ, cv2.TM_CCOEFF_NORMED)
         (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)

         if minloc[0] > 0:
              print('Карта не чиста')
              global stop
              global flag2
              stop = 1
              flag2 = False
              if t.is_alive():
                   print('Поток работает, убиваем', t.is_alive())

              else:
                   print('Поток спит, все ок', t.is_alive())

         else:
              print('Карта чиста')
              stop = 0
              flag2 = True
              if t.is_alive():
                   print('Поток работает, всё ок', t.is_alive())
              else:
                   print('Поток спал, запускаем', t.is_alive())
                   t.start()
                   k.start()
                   c.start()


flag = True
while flag:
    time.sleep(3)
    program()




