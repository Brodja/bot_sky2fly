import cv2
import pyautogui
from PIL import ImageGrab
import threading
import time

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




#
#
#
# #Поиск "Доки"
# time.sleep(2)
# screen_panel = ImageGrab.grab(bbox=(1790, 220, 1915, 550))
# screen_panel.save('/Users/admin/Pictures/testpil/screen_panel.png')
# screen_panel = cv2.imread('/Users/admin/Pictures/testpil/screen_panel.png')
# screen_doki = cv2.imread('/Users/admin/Pictures/testpil/Doki.png')
#
# result = cv2.matchTemplate(screen_panel, screen_doki, cv2.TM_CCOEFF_NORMED)
# (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
# pyautogui.click(x=maxloc[0] + 1790+5, y=maxloc[1] + 220+5)
#
# time.sleep(1)
# #Поиск "Корабль"
# screen_info = ImageGrab.grab(bbox=(900, 200, 1860, 750))
# screen_info.save('/Users/admin/Pictures/testpil/screen_info.png')
# screen_info = cv2.imread('/Users/admin/Pictures/testpil/screen_info.png')
# screen_button = cv2.imread('/Users/admin/Pictures/testpil/button1.png')
#
# result = cv2.matchTemplate(screen_info, screen_button, cv2.TM_CCOEFF_NORMED)
# (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
#
# pyautogui.click(x=maxloc[0] + 900, y=maxloc[1] + 200)
#
# time.sleep(1)
# #Поиск "Снаряжение"
# screen_info = ImageGrab.grab(bbox=(900, 200, 1860, 750))
# screen_info.save('/Users/admin/Pictures/testpil/screen_info.png')
# screen_info = cv2.imread('/Users/admin/Pictures/testpil/screen_info.png')
# screen_button = cv2.imread('/Users/admin/Pictures/testpil/button2.png')
#
# result = cv2.matchTemplate(screen_info, screen_button, cv2.TM_CCOEFF_NORMED)
# (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
# print(minloc, maxloc)
# pyautogui.click(x=maxloc[0] + 900, y=maxloc[1] + 200)
#
# time.sleep(1)
# #Поиск новой пилы
# screen_info = ImageGrab.grab(bbox=(900, 200, 1860, 750))
# screen_info.save('/Users/admin/Pictures/testpil/screen_info.png')
# screen_info = cv2.imread('/Users/admin/Pictures/testpil/screen_info.png')
# screen_button = cv2.imread('/Users/admin/Pictures/testpil/new_saw.png')
#
# result = cv2.matchTemplate(screen_info, screen_button, cv2.TM_CCOEFF_NORMED)
# (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
# print(minloc, maxloc)
# pyautogui.moveTo(maxloc[0] + 900, maxloc[1] + 200)
# pyautogui.dragTo(1590, 440,  button='left')
#
# time.sleep(1)
# #Поиск крестика
# screen_info = ImageGrab.grab(bbox=(900, 200, 1860, 750))
# screen_info.save('/Users/admin/Pictures/testpil/screen_info.png')
# screen_info = cv2.imread('/Users/admin/Pictures/testpil/screen_info.png')
# screen_button = cv2.imread('/Users/admin/Pictures/testpil/close.png')
#
# result2 = cv2.matchTemplate(screen_info, screen_button, cv2.TM_CCOEFF_NORMED)
# (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result2)
# print(minloc, maxloc)
# pyautogui.click(x=maxloc[0] + 900+3, y=maxloc[1] + 200+3)
# time.sleep(1)



#color_low = (100, 150, 200)
#color_high = (200, 250, 255)
#mapB = cv2.inRange(screen_takeO, color_low, color_high)
#takeB = cv2.inRange(take, color_low, color_high)

#cv2.imshow("Image", mapB)
#cv2.imshow("Image2", takeB)
#cv2.waitKey(0)