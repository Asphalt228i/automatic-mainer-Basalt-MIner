
import pyautogui
import time
import numpy as np

#"top": 356,"left": 306

a2 = int(input("видите top: "))

a3 = int(input("видите left: "))

a = {"top": a2,
     "left": a3,
     "width": 190,
     'height': 190,}


id = int(input("видите id шахты: "))




#color 1 [206,206,206] , color 2 [255,255,255], color 3 [0, 0 ,0]
def color_206(color206,b):

    a1 = np.array(b)

    our_map = (color206[2], color206[1], color206[0], 255)

    f1 = np.where(np.all(a1 == our_map, axis=-1))

    f3 = np.transpose(f1)

    return f3



def color_255(color2,b):

    a2 = np.array(b)

    our_map = (color2[2], color2[1], color2[0], 255)

    f11 = np.where(np.all(a2 == our_map, axis=-1))

    f33 = np.transpose(f11)

    return f33



def color_0(color0,b):

    a2 = np.array(b)

    our_map = (color0[2], color0[1], color0[0], 255)

    f11 = np.where(np.all(a2 == our_map, axis=-1))

    f33 = np.transpose(f11)

    return f33



def color_69(color69 , b):

    a2 = np.array(b)

    our_map = (color69[2], color69[1], color69[0], 255)

    f11 = np.where(np.all(a2 == our_map, axis=-1))

    f33 = np.transpose(f11)

    return f33



def color_251(color251,b):

    a2 = np.array(b)

    our_map = (color251[2], color251[1], color251[0], 255)

    f11 = np.where(np.all(a2 == our_map, axis=-1))

    f33 = np.transpose(f11)

    return f33


def color_70(color70,b):

    a2 = np.array(b)

    our_map = (color70[2], color70[1], color70[0], 255)

    f11 = np.where(np.all(a2 == our_map, axis=-1))

    f33 = np.transpose(f11)

    return f33


def color_200(color200, b):

    a2 = np.array(b)

    our_map = (color200[2], color200[1], color200[0], 255)

    f11 = np.where(np.all(a2 == our_map, axis=-1))

    f33 = np.transpose(f11)

    return f33



color255 = [255, 255, 255]#
color0 = [0, 0, 0]#
color206 = [206, 206, 206]#
color69 = [69, 69, 69]#
color251 = [251, 248, 247]#
color200 = [200, 199, 198]#
color70 = [70,70,70]


def id_1(a):
    while True:

        from mss import mss

        mss = mss()


        b = mss.grab(a)

        result = color_206(color206,b)

        if result.__len__():

                x = result[0][1] + a.get('left')

                y = result[0][0] + a.get('top')

                pyautogui.moveTo(x,y,1,pyautogui.easeOutQuad)

                time.sleep(1)

                pyautogui.mouseDown(button='right')

                time.sleep(1)

                pyautogui.mouseUp


        result1 = color_255(color255,b)

        if result1.__len__():

                x1 = result1[0][1] + a.get('left')

                y1 = result1[0][0] + a.get('top')

                pyautogui.moveTo(x1,y1,1,pyautogui.easeOutQuad)

                time.sleep(1)

                pyautogui.mouseDown(button='right')

                time.sleep(1)

                pyautogui.mouseUp



        result2 = color_0(color0,b)

        if result2.__len__():

                x2 = result2[0][1] + a.get('left')

                y2 = result2[0][0] + a.get('top')

                pyautogui.moveTo(x2,y2,1,pyautogui.easeOutQuad)

                time.sleep(1)

                pyautogui.mouseDown(button='right')

                time.sleep(1)

                pyautogui.mouseUp
        time.sleep(1)

def id_2(a):
    while True:
    #color [206,206,206]

        from mss import mss

        mss = mss()

        b = mss.grab(a)

        result = color_206(color206, b)

        if result.__len__():
            x = result[0][1] + a.get('left')

            y = result[0][0] + a.get('top')

            pyautogui.moveTo(x, y, 1, pyautogui.easeOutQuad)

            time.sleep(1)

            pyautogui.mouseDown(button='right')

            time.sleep(1)

            pyautogui.mouseUp









def id_3(a):
    #color 1 [251,248,247] , color 2 [206,206,206]
        while True:
            from mss import mss
            mss = mss()
            b = mss.grab(a)

            result = color_251(color251, b)

            if result.__len__():
                x = result[0][1] + a.get('left')

                y = result[0][0] + a.get('top')

                pyautogui.moveTo(x, y, 1, pyautogui.easeOutQuad)

                time.sleep(1)

                pyautogui.mouseDown(button='right')

                time.sleep(1)

                pyautogui.mouseUp



            result = color_206(color206, b)

            if result.__len__():
                x = result[0][1] + a.get('left')

                y = result[0][0] + a.get('top')

                pyautogui.moveTo(x, y, 1, pyautogui.easeOutQuad)

                time.sleep(1)

                pyautogui.mouseDown(button='right')

                time.sleep(1)

                pyautogui.mouseUp










def id_4(a):
    #color 1 [255,255,255] ,color 2 [69,69,69] color 3 [206,206,206]
    while True:
        from mss import mss
        mss = mss()
        b = mss.grab(a)


        result1 = color_255(color255, b)

        if result1.__len__():
            x = result1[0][1] + a.get('left')

            y = result1[0][0] + a.get('top')

            pyautogui.moveTo(x, y, 1, pyautogui.easeOutQuad)

            time.sleep(1)

            pyautogui.mouseDown(button='right')

            time.sleep(1)

            pyautogui.mouseUp



        result2 = color_69(color69, b)
        if result2.__len__():
            x1 = result2[0][1] + a.get('left')
            y2 = result2[0][0] + a.get('top')
            pyautogui.moveTo(x1, y2, 1, pyautogui.easeOutQuad)
            time.sleep(1)
            pyautogui.mouseDown(button='right')
            time.sleep(1)
            pyautogui.mouseUp



        result3 = color_206(color206, b)

        if result3.__len__():
             x = result3[0][1] + a.get('left')
             y = result3[0][0] + a.get('top')
             pyautogui.moveTo(x, y, 1, pyautogui.easeOutQuad)
             time.sleep(1)
             pyautogui.mouseDown(button='right')
             time.sleep(1)
             pyautogui.mouseUp




def id_5(a):
    #color 1 [206,206,206] color 2 [200,199,198]
    while True:
        from mss import mss

        mss = mss()

        b = mss.grab(a)

        result2 = color_206(color206, b)
        if result2.__len__():
            x1 = result2[0][1] + a.get('left')
            y2 = result2[0][0] + a.get('top')
            pyautogui.moveTo(x1, y2, 1, pyautogui.easeOutQuad)
            time.sleep(1)
            pyautogui.mouseDown(button='right')
            time.sleep(1)
            pyautogui.mouseUp


        result2 = color_200(color200, b)
        if result2.__len__():
            x1 = result2[0][1] + a.get('left')
            y2 = result2[0][0] + a.get('top')
            pyautogui.moveTo(x1, y2, 1, pyautogui.easeOutQuad)
            time.sleep(1)
            pyautogui.mouseDown(button='right')
            time.sleep(1)
            pyautogui.mouseUp









def id_6(a):
    #color 1 [206,206,206]
    while True:
        from mss import mss

        mss = mss()

        b = mss.grab(a)

        result2 = color_206(color206, b)
        if result2.__len__():
            x1 = result2[0][1] + a.get('left')
            y2 = result2[0][0] + a.get('top')
            pyautogui.moveTo(x1, y2, 1, pyautogui.easeOutQuad)
            time.sleep(1)
            pyautogui.mouseDown(button='right')
            time.sleep(1)
            pyautogui.mouseUp









def id_7(a):
    #color 1 [0,0,0] color 2 [69,69,69] color 3 [206,206,206]
    while True:
        from mss import mss

        mss = mss()
        b = mss.grab(a)

        result2 = color_0(color0, b)
        if result2.__len__():
            x1 = result2[0][1] + a.get('left')
            y2 = result2[0][0] + a.get('top')
            pyautogui.moveTo(x1, y2, 1, pyautogui.easeOutQuad)
            time.sleep(1)
            pyautogui.mouseDown(button='right')
            time.sleep(1)
            pyautogui.mouseUp


        result2 = color_69(color69, b)
        if result2.__len__():
            x1 = result2[0][1] + a.get('left')
            y2 = result2[0][0] + a.get('top')
            pyautogui.moveTo(x1, y2, 1, pyautogui.easeOutQuad)
            time.sleep(1)
            pyautogui.mouseDown(button='right')
            time.sleep(1)
            pyautogui.mouseUp


        result2 = color_206(color206, b)
        if result2.__len__():
            x1 = result2[0][1] + a.get('left')
            y2 = result2[0][0] + a.get('top')
            pyautogui.moveTo(x1, y2, 1, pyautogui.easeOutQuad)
            time.sleep(1)
            pyautogui.mouseDown(button='right')
            time.sleep(1)
            pyautogui.mouseUp














def id_8(a):
    #color 1 [206,206,206] color 2 [255,255,255] color 3 [69,69,69]
    while True:
        from mss import mss
        mss = mss()
        b = mss.grab(a)



        result1 = color_206(color206, b)
        if result1.__len__():
            x1 = result1[0][1] + a.get('left')
            y2 = result1[0][0] + a.get('top')
            pyautogui.moveTo(x1, y2, 1, pyautogui.easeOutQuad)
            time.sleep(1)
            pyautogui.mouseDown(button='right')
            time.sleep(1)
            pyautogui.mouseUp




        result2 = color_255(color255, b)
        if result2.__len__():
            x1 = result2[0][1] + a.get('left')
            y2 = result2[0][0] + a.get('top')
            pyautogui.moveTo(x1, y2, 1, pyautogui.easeOutQuad)
            time.sleep(1)
            pyautogui.mouseDown(button='right')
            time.sleep(1)
            pyautogui.mouseUp



        result3 = color_69(color69, b)
        if result3.__len__():
            x1 = result3[0][1] + a.get('left')
            y2 = result3[0][0] + a.get('top')
            pyautogui.moveTo(x1, y2, 1, pyautogui.easeOutQuad)
            time.sleep(1)
            pyautogui.mouseDown(button='right')
            time.sleep(1)
            pyautogui.mouseUp


def id_9(a):
    # color 1 [69,69,69] color 2 [0,0,0]
    while True:
        from mss import mss
        mss = mss()
        b = mss.grab(a)


        result1 = color_69(color69, b)
        if result1.__len__():
            x1 = result1[0][1] + a.get('left')
            y2 = result1[0][0] + a.get('top')
            pyautogui.moveTo(x1, y2, 1, pyautogui.easeOutQuad)
            time.sleep(1)
            pyautogui.mouseDown(button='right')
            time.sleep(1)
            pyautogui.mouseUp




        result2 = color_0(color0, b)
        if result2.__len__():
            x1 = result2[0][1] + a.get('left')
            y2 = result2[0][0] + a.get('top')
            pyautogui.moveTo(x1, y2, 1, pyautogui.easeOutQuad)
            time.sleep(1)
            pyautogui.mouseDown(button='right')
            time.sleep(1)
            pyautogui.mouseUp










def id_10(a):
    #color 1 [206,206,206]
    while True:
        from mss import mss
        mss = mss()
        b = mss.grab(a)

        result1 = color_206(color206, b)
        if result1.__len__():
            x1 = result1[0][1] + a.get('left')
            y2 = result1[0][0] + a.get('top')
            pyautogui.moveTo(x1, y2, 1, pyautogui.easeOutQuad)
            time.sleep(1)
            pyautogui.mouseDown(button='right')
            time.sleep(1)
            pyautogui.mouseUp














if id == 1:
    id_1(a)

if id == 2:
    id_2(a)

if id == 3:
    id_3(a)

if id == 4:
    id_4(a)

if id == 5:
    id_5(a)

if id == 6:
    id_6(a)

if id == 7:
    id_7(a)

if id == 8:
    id_8(a)

if id == 9:
    id_9(a)

if id == 10:
    id_10(a)

