import sys
import time
import win32api
import win32con
import random

def RandomGuess(xPos, yPos, scale) :
    scale = float(scale);
    xPos = float(xPos)
    yPos = float(yPos)
    posRandomGuess = []

    ranXVar = random.gauss(0.0, 1.0)
    ranXSclae = (scale*ranXVar)
    posRandomGuess.append(int(round(ranXSclae+xPos)))
    ranYVar = random.gauss(0.0, 1.0)
    ranYSclae = (scale*ranYVar)
    posRandomGuess.append(int(round(ranYSclae+yPos)))

    return posRandomGuess

def MouseClick(x, y) :
    x = int(x)
    y = int(y)
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def KeyboardClick(vk) :
    vk = int(vk)
    win32api.keybd_event(vk, 0)

def Delay(sec) :
    msec = float(sec) / 1000
    time.sleep(msec)

def main(lines, globalDelay, loop) :
    while loop > 1 or loop == -1 :
        # for line in lines:
            line = lines.split(' ')
            if(line[0].startswith('m')) :
                # Mouse Event
                testList = RandomGuess(line[1], line[2], 2)
                MouseClick(line[1], line[2])
            elif(line[0].startswith('k')) :
                # Keyboard Event
                KeyboardClick(line[1])
            elif (line[0].startswith('d')) :
                # Delay Event
                Delay(line[1])
            Delay(globalDelay)
            if loop != -1 : loop -= 1

main("m 10 10", 0, 10)


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