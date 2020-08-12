from wait import waitUntilFightSelection, \
  waitUntilModeSelection
from analyzeScreen import cookiesMessageOnScreen
from click import *
import time

def chooseT1():
  clickRanked()
  time.sleep(1)
  clickTourneyType1()

def chooseT2():
  clickRanked()
  time.sleep(1)
  clickTourneyType2()

def chooseFreeFight():
  clickPvP()
  time.sleep(1)
  clickFreeFight()

def choosePlayMode(gameMode):
  if gameMode == 'T1':
    chooseT1()
    
  elif gameMode == 'T2':
    chooseT2()

  elif gameMode == 'Free Fight':
    chooseFreeFight()

  else: print('This Playmode is not covered!')

def checkCookies():
  if cookiesMessageOnScreen():
    clickCookiesOk()
    time.sleep(1)
    clickCookiesOk()

# Tem que estar na tela inicial do jogo
def startGame(gameMode='T1'):
  print('In start game!')
  # if inURButNotInTheWebGLPage: clickPlayButton()
  clickWebGlButton()
  time.sleep(60)
  checkCookies()
  clickTouchToStart()
  waitUntilModeSelection()
  choosePlayMode(gameMode)  
  waitUntilFightSelection()
  # clickFight()

if __name__ == "__main__":
  startGame()
