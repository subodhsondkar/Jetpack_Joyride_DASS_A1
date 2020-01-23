import numpy as np
from obstacle import Firebeam, Coin, Magnet

def initialiseFirebeams(screen):
	firebeams = []
	x = screen.getScreenwidth() / 2 + 1
	while x < screen.getGamewidth():
		y = np.random.randint(0, screen.getScreenheight() - screen.getScreenheight() / 4)
		shape = np.random.randint(4)
		firebeam = Firebeam(x, y, shape)
		firebeams += [firebeam]
		firebeam.placeObstacle(screen)
		x += np.absolute(np.random.normal(screen.getScreenwidth() / 2, screen.getScreenwidth() / 2))
	return firebeams

def initialiseCoins(screen):
	coins = []
	x = screen.getScreenwidth() / 2
	while x < screen.getGamewidth():
		y = np.random.randint(0, screen.getScreenheight() - 1)
		coin = Coin(x, y)
		coins += [coin]
		coin.placeObstacle(screen)
		x += np.absolute(np.random.normal(screen.getScreenwidth() / 10, screen.getScreenwidth() / 10))
	return coins

def initialiseMagnets(screen):
	magnets = []
	x = screen.getScreenwidth()
	while x < screen.getGamewidth():
		y = np.random.randint(0, screen.getScreenheight() - 1)
		magnet = Magnet(x, y)
		magnets += [magnet]
		magnet.placeObstacle(screen)
		x += np.absolute(np.random.normal(screen.getScreenwidth(), screen.getScreenwidth()))
	return magnets
