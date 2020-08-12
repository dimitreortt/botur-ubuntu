""" Modulo para movimentos do mouse """
from quickGrab import *
import pyautogui as gui
import time

def leftClick():
  gui.click()
  time.sleep(0.1)
  print('Click')

def leftDown():
  gui.mouseDown()  
  print('Left down')

def leftUp():
  gui.mouseUp()  
  print('Left up')

def setMousePos(coord):
  print(x_pad + coord[0], y_pad + coord[1])
  gui.moveTo(x_pad + coord[0], y_pad + coord[1])

def getCoords():
  x,y = gui.position()
  x = x - x_pad
  y = y - y_pad
  print (x, y)
  return (x, y)

# getCoords()
# gui.click(interval=1)
# gui.mouseDown()
# gui.move(1900, 0)
# gui.mouseUp()



