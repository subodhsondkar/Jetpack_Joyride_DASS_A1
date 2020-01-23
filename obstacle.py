class Obstacle():
	def __init__(self, x, y, shape):
		self._base_x = int(x)
		self._base_y = int(y)
		self._shape = shape
		self._activated = 1
		self._on_time = 0
		return

	def getBase_x(self):
		return self._base_x

	def getBase_y(self):
		return self._base_y

	def getShape(self):
		return self._shape

	def getActivated(self):
		return self._activated

	def getOn_time(self):
		return self._on_time

	def enter(self):
		self._on_time += 1
		return

	def exit(self):
		self._on_time = 0
		return

class Firebeam(Obstacle):
	def placeObstacle(self, screen):
		if self._activated == 1:
			for i in range(int(screen.getScreenheight() / 4)):
				if self._shape == 0:
					try:
						screen.setGame(self._base_y + i, self._base_x - i, "F")
					except:
						pass
				elif self._shape == 1:
					try:
						screen.setGame(self._base_y + i, self._base_x, "F")
					except:
						pass
				elif self._shape == 2:
					try:
						screen.setGame(self._base_y + i, self._base_x + i, "F")
					except:
						pass
				else:
					try:
						screen.setGame(self._base_y, self._base_x + i, "F")
					except:
						pass
		return

	def collision(self, screen, player, is_player):
		if is_player == 1:
			player.killed()
		else:
			player.incrementPoints(16)
		if self._activated == 1:
			for i in range(int(screen.getScreenheight() / 4)):
				if self._shape == 0:
					try:
						screen.setGame(self._base_y + i, self._base_x - i, "H")
					except:
						pass
				elif self._shape == 1:
					try:
						screen.setGame(self._base_y + i, self._base_x, "H")
					except:
						pass
				elif self._shape == 2:
					try:
						screen.setGame(self._base_y + i, self._base_x + i, "H")
					except:
						pass
				else:
					try:
						screen.setGame(self._base_y, self._base_x + i, "H")
					except:
						pass
		self._activated = 0
		return

class Coin(Obstacle):
	def placeObstacle(self, screen):
		if self._activated == 1:
			screen.setGame(self._base_y, self._base_x, "C")
		return

	def collision(self, screen, player, is_player):
		if is_player == 1:
			player.incrementPoints(10)
		if self._activated == 1:
			screen.setGame(self._base_y, self._base_x, "H")
		self._activated = 0
		return

class Magnet(Obstacle):

	''' Concept ke in its range,
	either uppar ya neeche gravity jitna force aayega.
	Hence, in case of downward force,
	you can't go up even after clicking the "W" key.
	In case of upward force,
	you can't go down, basically free fall jesa. '''

	def placeObstacle(self, screen):
		if self._activated == 1:
			screen.setGame(self._base_y, self._base_x, "M")
		return

	def collision(self, screen, player, is_player):
		if is_player == 1:
			player.incrementPoints(2)
		else:
			player.incrementPoints(5)
		if self._activated == 1:
			screen.setGame(self._base_y, self._base_x, "H")
		self._activated = 0
		return
