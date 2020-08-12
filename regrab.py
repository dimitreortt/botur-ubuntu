from grab import *
import grab
import importlib

def reloadGrab():
  importlib.reload(grab)
  grab.reloadModules()
  importlib.reload(grab)
  grab.reloadModules()
  importlib.reload(grab)
  grab.reloadModules()
