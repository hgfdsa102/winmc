# -*- coding: utf-8 -*-
import sys
import time
import win32api
import win32con
import win32gui
import random
import lib.RandGen

def RandomGuessPos(xpos, ypos, scale):
    scale = float(scale)
    x_pos = float(xpos)
    y_pos = float(ypos)
    posRandomGuess = []
    ranXVar = random.gauss(0.0, 1.0)
    ran_x = (scale*ranXVar)
    posRandomGuess.append(int(round(ran_x+x_pos)))
    ranYVar = random.gauss(0.0, 1.0)
    ran_y = (scale*ranYVar)
    posRandomGuess.append(int(round(ran_y+y_pos)))
    return posRandomGuess


def RandomGuessDelay(msec, scale):
    scale = float(scale)
    msec = float(msec)
    ranSec = random.gauss(0.0, 1.0)
    ranSecSclae = (scale*ranSec)
    Delay(int(round(ranSecSclae+msec)))


def MouseClick(pos):
    x = int(pos[0])
    y = int(pos[1])
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def KeyboardClick(vk):
    vk = int(vk)
    win32api.keybd_event(vk, 0)


def Delay(sec):
    msec = float(sec) / 1000
    time.sleep(msec)


def main(lines, globalDelay, loop):
    while loop > 1 or loop == -1:
        line = lines.split(' ')
        if(line[0].startswith('m')):
            # Mouse Event
            testList = RandomGuessPos(line[1], line[2], 20)
            MouseClick(testList[0], testList[1])
        elif(line[0].startswith('k')):
            # Keyboard Event
            KeyboardClick(line[1])
        elif (line[0].startswith('d')):
            # Delay Event
            Delay(line[1])
        Delay(globalDelay)
        if loop != -1 : loop -= 1


def WindowExists(windowname):
    try:
        notehwnd = win32gui.FindWindow(None, windowname)
        print('handle', notehwnd)
    except win32gui.error:
        return False
    else:
        if notehwnd == 0:
            return False
        else:
            win32gui.SetForegroundWindow(notehwnd)  # 활성화
            return True


if WindowExists('[MOMO]앱플레이어'):
    print("Program is running")
    # main("m 400 500", 50, 0)
    testclass = lib.RandGen.RandGuass(0.0, 1.0)
    ary = testclass.RandomGuessPos(30, 30, 1)

    for i in range(1):
        # print(testclass.RandomGuessPos(30, 30, 5))
        MouseClick(testclass.RandomGuessPos(713, 410, 10))

    time.sleep(10)
else:
    print("Program is not running")
    time.sleep(10)


# if(len(sys.argv) == 2) :
#     f = open(sys.argv[1], 'r')
#     lines = f.readlines()
#     f.close()
#     main(lines, 0, 1)
# elif(len(sys.argv) == 4) :
#     f = open(sys.argv[1], 'r')
#     lines = f.readlines()
#     f.close()
#     gd = int(sys.argv[2])
#     loop = int(sys.argv[3])
#     # set mouse offset
#     main(lines, gd, loop)
# else :
#     print("must run with macro file")