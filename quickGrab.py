""" 
All coordinates assume a screen resolution of 1366x768, and Chrome 
maximized without the Bookmarks Toolbar enabled.
Only the slightiest white lane was kept above the blue baloon
to center the play area in browser.
x_pad = 113
y_pad = 120
Play area =  x_pad+1, y_pad+1, 796, 825
"""
#from PIL import ImageGrab
import pyscreenshot as ImageGrab
from PIL import ImageOps
from numpy import *

# import Image
#pip install pillowimport ImageGrab
import os
import time

meia_tela = False 
# Globals
if(meia_tela):
    x_pad = 20
    y_pad = 129
else:
    x_pad = 0
    y_pad = 0

def screenGrab():
  box = ()
  im = ImageGrab.grab(box)
  #im.save(os.getcwd() + '\\snapshots\\' + str(int(time.time())) + '.png', 'PNG')
  return im
 
def grabPlayArea(save=False):
  box = (x_pad + 1, y_pad + 1, x_pad + 1022, y_pad + 577)
  im = ImageGrab.grab(box)

  if save:
    im.save(os.getcwd() + '\\snapshots\\' + str(int(time.time())) + '.png', 'PNG')
    
  return im

def grabBox():
  box = (x_pad + 1,y_pad+1,x_pad+640,y_pad+480)
  im = ImageOps.grayscale(ImageGrab.grab(box))
  a = array(im.getcolors())
  a = a.sum()
  print(a)
  return a

def grabBubbleBox(i):
  i -= 1
  box = (x_pad + 25 + i * 101, y_pad + 60, x_pad +  86 + i * 101, y_pad +  74)
  im = ImageOps.grayscale(ImageGrab.grab(box))
  a = array(im.getcolors())
  a = a.sum()
  print(a)
  return a

def grabCustomBox(box, save = False):
  im = ImageGrab.grab(box)

  if save:
    im.save(os.getcwd() + '\\snapshots\\' + str(int(time.time())) + '.png', 'PNG')
    
  return im

def main():
    screenGrab()
 
if __name__ == '__main__':
    grabPlayArea()
    # print(grabBox())
