import pyautogui
import time
import numpy as np
print("видите left")
a2 = int(input())

print("видите top")

a3 = int(input())

a = {   "top": a2,
        "left": a3,
        "width": 190,
        'height': 190,}


def f(color, a = {}):
        from mss import mss
        mss = mss()

        b = mss.grab(a)


        a1 = np.array(b)
        our_map = (color[2], color[1], color[0], 255)
        f1 = np.where(np.all(a1 == our_map,axis=-1))

        f3 = np.transpose(f1)
        return f3

color = [206,206,206,255]



def f1(color1, a={}):
    from mss import mss
    mss = mss()

    b = mss.grab(a)

    a1 = np.array(b)
    our_map = (color1[2], color1[1], color1[0], 255)
    f1 = np.where(np.all(a1 == our_map, axis=-1))

    f3 = np.transpose(f1)
    return f3

color1 = [0, 0, 0, 255]



def f2(color2, a = {}):
        from mss import mss
        mss = mss()

        b = mss.grab(a)


        a1 = np.array(b)
        our_map = (color2[2], color2[1], color2[0], 255)
        f1 = np.where(np.all(a1 == our_map,axis=-1))

        f3 = np.transpose(f1)
        return f3

color2 = [255,255,255,255]



def f3(color3, a={}):
    from mss import mss
    mss = mss()

    b = mss.grab(a)

    a1 = np.array(b)
    our_map = (color3[2], color3[1], color3[0], 255)
    f1 = np.where(np.all(a1 == our_map, axis=-1))

    f3 = np.transpose(f1)
    return f3

color3 = [69,69,69,255]




while True:
#цвет серый(206,206,206)
        result = f(color, a)
        if result.__len__():
                x = result[0][1] + a.get('left')
                y = result[0][0] + a.get('top')
                pyautogui.moveTo(x,y,1,pyautogui.easeOutQuad)
                time.sleep(1)
                pyautogui.mouseDown(button='right')
                time.sleep(1)
                pyautogui.mouseUp


# функия 2 цвет(чёрный)
        result1 = f1(color1, a)
        if result1.__len__():
            x1 = result1[0][1] + a.get('left')
            y1 = result1[0][0] + a.get('top')
            pyautogui.moveTo(x1, y1, 1, pyautogui.easeOutQuad)
            time.sleep(1)
            pyautogui.mouseDown(button='right')
            time.sleep(1)
            pyautogui.mouseUp


#цвет белый
        result2 = f2(color2, a)
        if result2.__len__():
            x2 = result2[0][1] + a.get("left")
            y2 = result2[0][0] + a.get("top")
            pyautogui.moveTo(x2, y2, 1, pyautogui.easeOutQuad)
            time.sleep(1)
            pyautogui.mouseDown(button='right')
            time.sleep(1)
            pyautogui.mouseUp


#серый цвет(69,69,69)
        result3 = f3(color3, a)
        if result3.__len__():
            x3 = result3[0][1] + a.get("left")
            y3 = result3[0][0] + a.get("top")
            pyautogui.moveTo(x3, y3, 1, pyautogui.easeOutQuad)
            time.sleep(1)
            pyautogui.mouseDown(button='right')
            time.sleep(1)
            pyautogui.mouseUp

        time.sleep(1)
