from click import *
from analyzeScreen import *

def waitMyTurn():
  count = 0
  while True:    
    count += 1
    
    if count % 3 == 0:
      clickBlankSpace()

    if inEndMatch():
      print('Battle Ended!')
      return 'Battle Ended!'
    
    elif inBattleHasTimeout():
      print('Battle has timeout!')
      return 'Timeout'

    elif errorMessageOnScreen():
      print('Error message on screen!')
      return 'Error Message!'

    elif inTurn():
      print('In Turn!!')

      mustPass = myTurn()
      if mustPass != 'Not in turn!':
        while not mustPass:
          print('Not my turn!')

          mustPass = myTurn()
          if mustPass == 'Not in turn!':
            print('Not even in turn!')
            break

          clickBlankSpace()
          time.sleep(1)

        if mustPass != 'Not in turn' and mustPass:
          print('In my turn!')
          return 'My Turn'

    else:
      print('Not in turn!')
      time.sleep(2)
      if count == 100:
        return 'Loop infinito!'

def waitMyTurnFourTimes():
  for i in range(3):
    print('gonna wait my turn for the %dª time' % i)
    time.sleep(1)

    result = waitMyTurn()
    if result != 'My Turn':
      return result
  
  return result

def waitEndMatch():
  print('\n  # -- Waiting end match! -- #\n')
  count = 0
  while(not inEndMatch()):
    if count == 100:
      return 'Restart page and bot!'
    else:
      count += 1

    print('Not in end match!')

    if count % 2 == 0:
      clickBlankSpace()

    if inTurn() and not myTurn():
      print('In turn, but not my turn!')

    elif inTurn() and myTurn():
      return 'Play all cards with 0 pillz!'

    elif(inBattleHasTimeout()):
      print('Battle has timeout!')
      clickTimeoutOK()
      # waitEndMatch()

    elif(errorMessageOnScreen()):
      print('Error message on screen!')
      clickTimeoutOK()
      # waitEndMatch()

    elif(inFightSelection()):
      print('Something is wrong! We are in fightSelection but this page should have been gone! It is probably a problem of deck type, is it designed for T1 or T2??\n')
      print('Exiting...')
      exit(1)

    elif(stuckInMatchMaking()):
      return 'Restart page and bot!'

    else:
      print('Not in my turn nor battle has timeout!')
      scan = scanUnexpectedPages()
      if scan == 'Fight Selection!' or scan == 'Play Again!':
        return
    
    time.sleep(1.5)
scanCount = 0
# Vai fazer muitos prints sem espera,
# sobrecarrega o programa mas é uma parte
# crítica!
def waitNotMyTurn():
  print('waitNotMyTurn()')
  count = 0
  while(inTurn() and myTurn()):
    count += 1
    if count == 10:
      return
    clickBlankSpace()

    pass
  print('leaving waitNotMyTurn()!')

def waitUntilFightSelection():
  count = 0
  while(not inFightSelection()):
    if count == 60:
      # print('runBot() was unable to reach fightSelection! Exiting...')
      print('Deixando uma bucha para o playMatch resolver!')
      exit()

    count += 1

    print('Not in Fight Selection')
    time.sleep(2)
  
  print('In Fight Selection')

def waitUntilModeSelection():
  # clickWebGlButton() # Click to start  
  count = 0
  while(not inModeSelection()):
    if count == 60:
      print('runBot() was unable to reach modeSelection! Exiting...')
      exit()

    count += 1

    print('Not in Mode Selection')
    time.sleep(2)

  print('In Mode Selection')
