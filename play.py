from random import randint
from numpy import setdiff1d
from click import *
from wait import *
from pillz import getPillzSet
from startGame import startGame
from gameMode import getModeInput
from coordinates import *

def playAllCardsWith0Pillz():
  for i in range(4):
    playCard(i, 0)

cards = [0, 1, 2, 3]
cardsPlayed = []
def nextCard():
  availableCards = setdiff1d(cards, cardsPlayed)
  nextcard = availableCards[randint(0, len(availableCards) - 1)]
  cardsPlayed.append(nextcard)
  return nextcard

def resetCardsPlayed():
  global cardsPlayed
  cardsPlayed = []
  print('Cards reset!')  

def playCard(cardIndex, pillzNumber):
  cardIndexCoords = GameItemsCoords.Cards[cardIndex]
  print("Next card chosen is %d, coords:" % (cardIndex),cardIndexCoords)
  pillzNumberCoords = GameItemsCoords.Pillz[pillzNumber-1]
  print("Number of Pillz is", pillzNumber, "coords:", pillzNumberCoords)
  clickCard(cardIndex)
  time.sleep(2)
  if not inCardClicked():
    clickCard(cardIndex)
    time.sleep(2)
  
  if(pillzNumber != 0):
    time.sleep(0.5)  
    clickAddPillz(pillzNumber)
    print('Cliquei em addPillz e vou esperar 1.5 segundos')
    time.sleep(1.5)

  time.sleep(0.5)
  clickFightRound()

def clickPlay():
  if inFightSelection():
    clickFight()

  elif inEndMatch():
    clickPlayAgain()
    # Esse tempo é importantíssimo para a lógica
    # observe o loop principal, sem esse tempo, o loop
    # pode crashar pois o waitMyTurn vai achar que o game acabou,
    # antes de sequer começar
    count = 0
    while(not inTurn()):
      time.sleep(2)
      if count == 60:
        if inMatchMaking():
          clickCancelMatchMaking()
        return
        
      if count % 5 == 0:
        if not inMatchMaking():
          clickPlayAgain()
        
      count += 1

  else:
    print('There is no clickPlay option!!')

def restartPageAndBot():
  print('\n  XXX -- I am going to restart Page & Bot! -- XXX\n')
  clickReloadPage()
  time.sleep(15)
  runBot()

def playMyTurn(pillzNumber):
  print('\n # - Decided it is my turn!! - #\n')
  # time.sleep(2)

  playCard(nextCard(), pillzNumber)
  time.sleep(5)
  waitNotMyTurn()

def treatEndMatchStatus(endStatus):
  if endStatus == 'Restart page and bot!':
    restartPageAndBot()

  elif endStatus == 'Play all cards with 0 pillz!':
    playAllCardsWith0Pillz()

def waitUntilEndMatch():
  endStatus = waitEndMatch()
  treatEndMatchStatus(endStatus)

def playMatch():
  resetCardsPlayed()
  pillzSet = getPillzSet()
  print(pillzSet)
  clickPlay()

  for i in range(4):
    situation = waitMyTurnFourTimes()
    if situation == 'Battle Ended!':
      return

    elif situation == 'Timeout':
      clickTimeoutOK()
      break

    elif situation == 'Error Message!':
      clickTimeoutOK()
      break

    elif situation == 'Loop Infinito!':
      return 

    elif situation == 'My Turn':
      playMyTurn(pillzSet[i])
      
    else:
      return print('Error! Situation not identified!')

  waitUntilEndMatch()  

gameMode = 'Free Fight'
def runBot():
  global gameMode
  startGame(gameMode)
  playForever()

def setUpGameMode():
  global gameMode
  gameMode = getModeInput()

def playForever():
  while True:
    playMatch()

def play():
  setUpGameMode()
  playForever()

if __name__ == "__main__":
  play()
