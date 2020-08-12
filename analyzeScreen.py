from coordinates import BoxesCoords, ButtonsCoords, GameItemsCoords
from pixels import getColorSum, ColorSums, getColorSumeExcluaPorFavor, saveImage
from pixels import ButtonPixels
from quickGrab import screenGrab, grabPlayArea
import time
from click import clickBlankSpace, clickTimeoutOK

def checkMyBackground():
  return getColorSum(BoxesCoords.MyBackground)

def checkOpponentsBackground():
  return getColorSum(BoxesCoords.OpponentsBackground)
  # background = getColorSum(BoxesCoords.)

def checkMyDashBoard():
  return getColorSum(BoxesCoords.MyPlayerDashBoard)

def checkEndMatch():
  return getColorSum(BoxesCoords.EndMatch)

def inPlayAgain():
  return getColorSum(BoxesCoords.PlayAgain) in ColorSums.PlayAgain

def inCardClicked():
  return getColorSum(BoxesCoords.FightRound) in ColorSums.FightRound

def inMatchMaking():
  return getColorSum(BoxesCoords.MatchMakingCancel) in ColorSums.MatchMakingCancel
  pass

def cookiesMessageOnScreen():
  im = screenGrab()
  return im.getpixel(ButtonsCoords.CookiesBoxBlankSpace) == ButtonPixels.CookiesBoxBlankSpace

def errorMessageOnScreen():
  im = screenGrab()
  #print("In errorMessageOnScreen, imPixel:", im.getpixel(GameItemsCoords.ErrorOK), "Error OK pixel:", ButtonPixels.ErrorOK)
  return im.getpixel(GameItemsCoords.ErrorOK) == ButtonPixels.ErrorOK

def cardInfoOnScreen():
  return getColorSum(BoxesCoords.CardInfo) in ColorSums.CardInfo

def loopCardInfoOnScreen():
  while True:
    print(cardInfoOnScreen())
    time.sleep(0.3)

def inEndMatch():
  print('Checking end match...')
  if(getColorSum(BoxesCoords.EndMatch) in ColorSums.EndMatch):
    print('Endmatch!')
    return True
  
  elif(inPlayAgain()):
    print('I didnt find the end match, \
    but i found the play again, so I am returning true...')
    return True
  # if errorMessageOnScreen():
  #   clickTimeoutOK()

  else:
    clickTimeoutOK()
  return False

def inBattleHasTimeout():
  return getColorSum(BoxesCoords.TheBattleHasTimeout) == ColorSums.TheBattleHasTimeout

def inModeSelection():
  return getColorSum(BoxesCoords.ModeSelectionLogo) in ColorSums.ModeSelectionLogo

def inFightSelection():
  return getColorSum(BoxesCoords.Fight) == ColorSums.Fight

def inTurn():
  return getColorSum(BoxesCoords.MyPlayerDashBoard) in ColorSums.MyDashBoard

def loopInTurn():
  while True:
    print(inTurn())

def myTurn():
  if not inTurn():
    print('Error! Not in turn, imagine in mine! -> We are fighting!')
    return 'Not in turn!'

  soma, fullsnap = getColorSumeExcluaPorFavor(BoxesCoords.MyTurnArrowBox)
  if soma not in ColorSums.MyTurnArrowBoxEmpty:
    # saveImage(fullsnap)
    return True

  return False

  # return getColorSum(BoxesCoords.MyBackground) != ColorSums.MyBackground

def scanUnexpectedPages():
  print('Scanning unexpected pages...')
  if inFightSelection():
    return 'Fight Selection!'

  elif inPlayAgain():
    return 'Play Again!'

  elif inModeSelection():
    # return 'Mode Selection'    # não posso retratar tudo em todo lugar!
    pass  

  elif cardInfoOnScreen():
    clickBlankSpace()

def stuckInMatchMaking():
  for i in range(10):
    if not getColorSum(BoxesCoords.StuckMatchMaking) in ColorSums.StuckMatchMaking:
      return False

    time.sleep(2)
  return True
