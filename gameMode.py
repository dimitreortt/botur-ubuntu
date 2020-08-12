def modeExists(mode):
  return mode in ['Free Fight', 'T1', 'T2']

def modeInput():
  return input('What game mode do you want to play? Free Fight, T1, T2... ? ')

def anotherModeInput():
  return input('This mode does node exist! Please choose another! ')

def getModeInput():
  mode = modeInput()
  while not modeExists(mode):    
    mode = anotherModeInput()

  return mode
