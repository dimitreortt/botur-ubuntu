import random
from random import randint

class PossiblePilling():
  possibles = [
    (3, 3, 3, 3),
    (5, 4, 3, 0),
    (3, 4, 5, 0),
    (3, 7, 2, 0),
    (4, 4, 4, 0),
    (6, 6, 0, 0),
    (0, 6, 6, 0),
    (0, 6, 0, 6),
    (6, 0, 6, 0),
    (2, 5, 5, 0),
    (5, 2, 5, 0),
    (7, 5, 0, 0),
    (6, 3, 3, 0),
    (4, 4, 0, 4)
  ]

def randBool():
  return random.choice([True, False])

def TypePillzSet(type):
  return random.choice(PossiblePilling.possibles)
  if type == 'Type1':
    r1 = randint(2, 4)
    r2 = randint(1, 6 - r1)
    # r3 = 12 - r2 - r1
    r3 = randint(2, 9 - r2 - r1)
    # r4 = randint(11 - r3 - r2 - r1, 12 - r3 - r2 - r1)
    r4 = 12 - r3 - r2 - r1

    return (r1, r2, r3, r4)

  elif type == 'Type2': # -> Type 2 ta zuadasso!
    if randBool():
      # jogar 2hko
      return (6, 0, 6, 0) if randBool() and randBool() else (6, 6, 0, 0)

    # r1 = 0 if (randBool() and randBool()) else randint(3, 6)
    r1 = randint(3, 6)

    if(r1 == 0):
      r2 = randint(5, 8 - r1)
    else:
      r2 = randint(2, 9 - r1)
      
    r3 = 12 - r2 - r1
    # r3 = randint(0, 10 - r2 - r1)
    # r4 = randint(11 - r3 - r2 - r1, 12 - r3 - r2 - r1)
    r4 = 12 - r3 - r2 - r1

    return (r1, r2, r3, r4)

def getPillzSet():
  return TypePillzSet('Type1')  