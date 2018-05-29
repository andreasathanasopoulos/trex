import pyautogui
from time import sleep
import pyscreenshot as ImageGrab

import PIL.Image # python-imaging
import PIL.ImageStat # python-imaging
import Xlib.display # python-xlib
import numpy

import time
time.clock()
# image = ImageGrab.grab()
# color = image.getpixel((794, 706))
# print(image)
# print(color)
# exit()
# for y in range(0, 794, 700):
#     for x in range(0, 1260, 700):
#         color = image.getpixel((x, y))
# print(color)
# print(time.clock())
# exit()

def get_pixel_colour(i_x, i_y):
    o_x_root = Xlib.display.Display().screen().root
    o_x_image = o_x_root.get_image(i_x, i_y, 1, 1, Xlib.X.ZPixmap, 0xffffffff)
    o_pil_image_rgb = PIL.Image.frombytes("RGB", (1, 1), o_x_image.data, "raw", "BGRX")
    lf_colour = PIL.ImageStat.Stat(o_pil_image_rgb).mean
    lf_colour = sum(lf_colour)
    # return tuple(map(int, lf_colour))
    return lf_colour

def main():
    """ Main program """
    pyautogui.moveTo(960, 770)
    pyautogui.click()
    o_x_root = Xlib.display.Display().screen().root
    speedx = 840
    step = 15
    while True:
        # print(get_pixel_colour(850, 795)) # obstacle 799 745
        # o_x_image = o_x_root.get_image(840, 801, 1, 2, Xlib.X.ZPixmap, 0xffffffff)
        # print(int(time.clock()))
        if int(time.clock()) % step == 0:
            speedx += 3
            print(speedx)
            step += 15
        # o_x_image = o_x_root.get_image(speedx, 805, 3, 3, Xlib.X.ZPixmap, 0xffffffff)
        o_x_image = o_x_root.get_image(speedx, 801, 1, 2, Xlib.X.ZPixmap, 0xffffffff)
        o_pil_image_rgb = PIL.Image.frombytes("RGB", (1, 1), o_x_image.data, "raw", "BGRX")
        lf_colour = PIL.ImageStat.Stat(o_pil_image_rgb).mean
        lf_colour = sum(lf_colour)
        o_x_image2 = o_x_root.get_image(speedx, 769, 2, 2, Xlib.X.ZPixmap, 0xffffffff)
        o_pil_image_rgb2 = PIL.Image.frombytes("RGB", (1, 1), o_x_image2.data, "raw", "BGRX")
        lf_colour2 = PIL.ImageStat.Stat(o_pil_image_rgb2).mean
        lf_colour2 = sum(lf_colour2)
        # print(lf_colour)
        if lf_colour < 741.0 or lf_colour > 741.0:
            # print('JUMP')
            pyautogui.keyDown('up')
            sleep(0.05)
            pyautogui.keyUp('up')
        if lf_colour2 < 741.0 or lf_colour2 > 741.0:
            pyautogui.keyDown('up')
            sleep(0.05)
            pyautogui.keyUp('up')
        # sleep(0.05)
    return 0

if __name__ == "__main__":
    main()
