import os
#from PIL import ImageGrab
import pyscreenshot as ImageGrab
from PIL import ImageOps
from numpy import *
import time
from coordinates import GameItemsCoords as gic 

class ButtonPixels():
  ErrorOK = (255, 160, 0)
  CookiesOK = (14, 44, 42)
  CookiesBoxBlankSpace = (204, 232, 234)

class PillzPixels():
  # Decidi fazer por faixas
  # Faixa Disponível -> (59, 49, 52), (65, 54, 57)
  # Faixa Indisponível -> (20, 20, 20), (26, 26, 26)
  # Faixa Adicionado -> (190, 0, 208) (230, 5, 224)
  AvailableMargin = ((59, 49, 52), (65, 54, 57))
  UnAvailableMargin = ((20, 20, 20), (26, 26, 26))
  AddedMargin = ((180, 0, 208), (230, 5, 224))

def getPillzNumberCoords(pillzNumber):
  pcoord = gic.Pillz[pillzNumber]
  return getPixel(pcoord)

def pixelInsideMargin(pixel, margin):
  lowerBound, upperBound = margin

  if pixel[0] < lowerBound[0] or pixel[0] > upperBound[0]:
    print(pixel)
    return False
    
  if pixel[1] < lowerBound[1] or pixel[1] > upperBound[1]:
    print(pixel)
    return False
    
  if pixel[2] < lowerBound[2] or pixel[2] > upperBound[2]:
    print(pixel)
    return False
        
  return True

def getPillzAvailable():
	pillzAvailable = 0
	for i in range(12):
		if isPillzNumberAvailable(i):
			pillzAvailable += 1
		else:
			return pillzAvailable	  
	
	return pillzAvailable

def getPillzAdded():
	pillzAdded = 0
	for i in range(12):
		if isPillzNumberAdded(i):
			pillzAdded += 1
		else:
			return pillzAdded
	
	return pillzAdded

def isPillzNumberUnAvailable(pillzNumber):
  pixel = getPillzNumberCoords(pillzNumber)
  margin = PillzPixels.UnAvailableMargin
	
  return pixelInsideMargin(pixel, margin)

def isPillzNumberAvailable(pillzNumber):
  pixel = getPillzNumberCoords(pillzNumber)
  margin = PillzPixels.AvailableMargin
	
  return pixelInsideMargin(pixel, margin)
  
def isPillzNumberAdded(pillzNumber):
  pixel = getPillzNumberCoords(pillzNumber)
  margin = PillzPixels.AddedMargin
  
  return pixelInsideMargin(pixel, margin)

class ColorSums():
  # GameModes = 41435
  GameModes = 38565 #38373 #38767
  Fight = 21096
  MyBackground = 10718
  MyTurnArrowBoxEmpty = (5555, -1)
  MyDashBoard = (5616, -1)
  EndMatch = (2701, 4709, 3095, -1)
  PlayAgain = (25168, 25033)
  TheBattleHasTimeout = 26537
  CardInfo = (2121, -1)
  StuckMatchMaking = (39924, -1)
  ModeSelectionLogo = (23651, -1)
  MatchMakingCancel = (11179,-1)
  FightRound = (19153, -1)

# Deve receber a box em coordenadas globais!
def getColorSum(box, save=False):

  bx1, by1, bx2, by2 = box
  # print(x_pad, y_pad)
  box = (bx1, by1, bx2, by2)
  # print(box)
  im = ImageGrab.grab(box)
  if save:
    print("vou salvar aqui:",os.getcwd() + '\\snapshots\\' + str(int(time.time())) + '.png', 'PNG')
    im.save(os.getcwd() + '/snapshots/' + str(int(time.time())) + '.png', 'PNG')

  im = ImageOps.grayscale(im)
  a = array(im.getcolors())
  a = a.sum()
  # print(a)
  return a

# Deve receber a box em coordenadas globais!
def getColorSumeExcluaPorFavor(box, save=False):

  bx1, by1, bx2, by2 = box
  # print(x_pad, y_pad)
  box = (bx1, by1, bx2, by2)
  # print(box)
  im = ImageGrab.grab(box)
  fullsnap = ImageGrab.grab()
  if save:
    im.save(os.getcwd() + '\\snapshots\\' + str(int(time.time())) + '.png', 'PNG')
  else: 
    pass
#    print('ooooo carniça veia kakaka')

  im = ImageOps.grayscale(im)
  a = array(im.getcolors())
  a = a.sum()
  # print(a)
  return a, fullsnap

def saveImage(im):
  im.save(os.getcwd() + '\\snapshots\\' + str(int(time.time())) + '.png', 'PNG')
  
def getPixel(coord, im=''):
  if not im:
    im = ImageGrab.grab()
  return im.getpixel(coord)
