""" Modulo exclusivo para recarregar os módulos em tempo
de execução. Não alterar o conteúdo! """

import importlib
import quickGrab
import mouse
import startGame
import coordinates
import pixels
import play
import wait
import analyzeScreen
import click


def reloadModules():
  importlib.reload(quickGrab)
  importlib.reload(mouse)
  importlib.reload(startGame)
  importlib.reload(coordinates)
  importlib.reload(pixels)
  importlib.reload(play)
  importlib.reload(wait)
  importlib.reload(analyzeScreen)
  importlib.reload(click)

  
if __name__ == '__main__':
  print('1')
