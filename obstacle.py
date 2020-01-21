class Obstacle():
	def __init__(self, x, y, shape):
		self._base_x = int(x)
		self._base_y = int(y)
		self._shape = shape
		self._activated = 1
		return

	def getBase_x(self):
		return self._base_x

	def getBase_y(self):
		return self._base_y

	def getShape(self):
		return self._shape

	def getActivated(self):
		return self._activated

class Firebeam(Obstacle):
	def placeObstacle(self, screen):
		if self._activated is 1:
			for i in range(int(screen.getScreenheight() / 4)):
				if self._shape is 0:
					try:
						screen.setGame(self._base_y + i, self._base_x - i, "F")
					except:
						print(self._shape, self._base_x - i, self._base_y + i)
				elif self._shape is 1:
					try:
						screen.setGame(self._base_y + i, self._base_x, "F")
					except:
						print(self._shape, self._base_x, self._base_y + i)
				elif self._shape is 2:
					try:
						screen.setGame(self._base_y + i, self._base_x + i, "F")
					except:
						print(self._shape, self._base_x + i, self._base_y + i)
				else:
					try:
						screen.setGame(self._base_y, self._base_x + i, "F")
					except:
						print(self._shape, self._base_x + i, self._base_y)
		return

	def deactivateObstacle(self, screen):
		if self._activated is 1:
			for i in range(int(screen.getScreenheight() / 4)):
				if self._shape is 0:
					screen.setGame(self._base_y + i, self._base_x - i, "H")
				elif self._shape is 1:
					screen.setGame(self._base_y + i, self._base_x, "H")
				elif self._shape is 2:
					screen.setGame(self._base_y + i, self._base_x + i, "H")
				else:
					screen.setGame(self._base_y, self._base_x + i, "H")
		self._activated = 0
		return

	def collision(self, screen, hero):
		hero.killed()
		self.deactivateObstacle(screen)
		return

class Coin(Obstacle):
	def placeObstacle(self, screen):
		if self._activated is 1:
			screen.setGame(self._base_y, self._base_x, "C")
		return

	def deactivateObstacle(self, screen):
		if self._activated is 1:
			screen.setGame(self._base_y, self._base_x, "H")
		self._activated = 0
		return

	def collision(self, screen, hero):
		hero.incrementPoints(1)
		self.deactivateObstacle(screen)
		return

class Magnet(Obstacle):
	''' Concept ke in its range,
	either uppar ya neeche gravity jitna force aayega.
	Hence, in case of downward force,
	you can't go up even after clicking the "W" key.
	In case of upward force,
	you can't go down, basically free fall jesa. '''
	pass
