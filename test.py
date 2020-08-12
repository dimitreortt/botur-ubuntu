#from selenium.webdriver import Firefox
#from selenium.webdriver.firefox.options import Options

#opts = Options()
#opts.set_headless()
#assert opts.headless  # Operating in headless mode
#browser = Firefox(options=opts)
#browser.get('https://www.urban-rivals.com/game/play/')

#search_form = browser.find_element_by_id('search_form_input_homepage')
#search_form.send_keys('real python')
#search_form.submit()

#browser.close()

from coordinates import GameItemsCoords as gic
#from pixels import getPixel, isPillzNumberAvailable, isPillzNumberAdded,isPillzNumberUnAvailable, getPillzAvailable
from pixels import *
from click import setMousePos, leftClick

def getPillzPixels():
	#pillzPixels = []
	#for i in range(12):
	  #pcoord = gic.Pillz[i]
	  #pixel = getPixel(pcoord)
	  #setMousePos(pcoord)
	  ##leftClick()
	  #print('it', i, ', pcoord', pcoord, ', pixel', pixel)
	  #pillzPixels.append(pixel)

	#print(pillzPixels)
	pass

def testIsPillzAvailable():
	for i in range(12):
		print(isPillzNumberAvailable(i))
		
def testIsPillzAdded():
	for i in range(12):
		print(isPillzNumberAdded(i))

def testIsPillzUnAvailable():
	for i in range(12):
		print(isPillzNumberUnAvailable(i))
		
if __name__ == "__main__":
  #testIsPillzAvailable()
  #testIsPillzAdded()
  #testIsPillzUnAvailable()
#  print(getPillzAvailable())
  print(getPillzAdded())
  pass
  

