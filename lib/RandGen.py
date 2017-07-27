import time
import win32api
import win32con
import random


class RandGuass:
    def __init__(self):
        self.mu = 0.0
        self.sigma = 1.0


    def RandomGuessPos(self, xpos, ypos, scale):
        scale = float(scale)
        x_pos = float(xpos)
        y_pos = float(ypos)
        posRandomGuess = []
        ranXVar = random.gauss(0.0, 1.0)
        ran_x = (scale * ranXVar)
        posRandomGuess.append(int(round(ran_x + x_pos)))
        ranYVar = random.gauss(0.0, 1.0)
        ran_y = (scale * ranYVar)
        posRandomGuess.append(int(round(ran_y + y_pos)))
        return posRandomGuess


    def RandomGuessDelay(self, msec, scale):
        scale = float(scale)
        msec = float(msec)
        ranSec = random.gauss(0.0, 1.0)
        ranSecSclae = (scale * ranSec)
        self.Delay(int(round(ranSecSclae + msec)))


    def Delay(self, sec):
        msec = float(sec) / 1000
        time.sleep(msec)