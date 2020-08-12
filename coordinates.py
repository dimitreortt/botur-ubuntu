#from quickGrab import x_pad, y_pad

# Coordenadas de Play Area
class ButtonsCoords():
  WebGl = (430, 570)
  Ranked = (663, 209)
  PvP = (565, 204)
  Type1 = (545, 308)
  Type2 = (617, 303)
  Survivor = (554, 470)
  FreeFight = (566, 340)
  Fight = (429, 566)
  TouchToStart = (423, 489)  
  PlayAgain = (437, 567)
  Reload = (159, 122)  
  Solo = (463, 206)
  MissionsOK = (431, 484)
  CancelMatchMaking = (750, 216)
  CookiesOk = (663, 539)
  CookiesBoxBlankSpace = (587, 538)

# Coordenadas Globais
class BoxesCoords():
  # GameModesNavbarBox = (580, 129, 1143, 150)
  GameModesNavbarBox = (660, 125, 1060, 150)
  Fight = (393, 557, 469, 573)
  MyBackground = (707, 553, 729, 565)
  OpponentsBackground = (274, 122, 290, 140)
  MyPlayerDashBoard = (585, 550, 650, 563)
  MyTurnArrowBox = (707, 553, 729, 565)
  EndMatch = (568, 455, 659, 478)
  PlayAgain = (610, 643, 738, 662)
  TheBattleHasTimeout = (225,356, 377, 369)
  CardInfo = (789, 497, 822, 513)
  StuckMatchMaking = (920, 120, 1078, 168)
  ModeSelectionLogo = (90,198, 291, 215)
  MatchMakingCancel = (725, 211, 772,223)
  FightRound = (486, 440, 557, 459)
# (915, 61)
# (757, 13)
# x_pad = 163
# y_pad = 107
class GameItemsCoords():
  Card1 = (268, 432)
  Card2 = (384, 450)
  Card3 = (483, 490)
  Card4 = (602, 443)


  Cards = [Card1, Card2, Card3, Card4]

  Pillz = [
  (367, 392), (385, 392), (403, 392),
  (421, 392),
  (440, 392),
  (459, 392),
  (479, 392),
  (496, 392),
  (515, 392),
  (534, 392),
  (552, 392),
  (569, 392),  
  ]

  Fury = (832, 299)
  FightRound = (521, 453) #

  TimeOutOK = (431, 453)
  ErrorOK = (433, 463)
  BlankSpace = (485, 516)

def generatePillzCoords():
    start = 578
    pillz = [start]
    soma = 0
    for i in range(11):
      soma += 27
      if i in [2, 5, 8, 10]:
        soma -= 1
      pillz.append(start+soma)
    
    return [(item - x_pad, 409 - y_pad) for item in pillz]
  
if __name__ == "__main__":
  pass
