import time

class Hero():
	def __init__(self, screen, x, y):
		self._base_x = x
		self._base_y = y
		self._x_velocity = 2
		self._y_velocity = 0
		self._score = 0
		self._lives = 3
		self._shield = 0
		self._shield_on_time = 5
		self._shield_recharge_time = 10
		self._shield_time = time.time() - self._shield_recharge_time
		self.placeHero(screen)
		return

	def getBase_x(self):
		return self._base_x

	def getBase_y(self):
		return self._base_y

	def getScore(self):
		return self._score

	def getLives(self):
		return self._lives

	def getShield(self):
		return self._shield

	def activateShield(self):
		self._shield = 1
		return

	def deactivateShield(self):
		self._shield = 0
		return

	def killed(self):
		if self._shield is 1:
			return
		elif self._lives > 1:
			self._lives -= 1
		else:
			print("Score:", self._score)
			input()
			exit()
		return

	def incrementPoints(self, points):
		self._score += points
		return

	def removeHero(self, screen):
		screen.setGame(int(self._base_y) - 2, int(self._base_x), "H")
		screen.setGame(int(self._base_y) - 1, int(self._base_x), "H")
		screen.setGame(int(self._base_y) - 1, int(self._base_x) + 1, "H")
		screen.setGame(int(self._base_y), int(self._base_x), "H")
		return

	def placeHero(self, screen):
		screen.setGame(int(self._base_y) - 2, int(self._base_x), "O")
		screen.setGame(int(self._base_y) - 1, int(self._base_x), "|")
		screen.setGame(int(self._base_y) - 1, int(self._base_x) + 1, "<")
		screen.setGame(int(self._base_y), int(self._base_x), "^")
		return

	def collisionCheck(self, screen, obstacle, i, j):
		if int(self._base_x) == obstacle.getBase_x() + i and int(self._base_y) == obstacle.getBase_y() + j or int(self._base_x) == obstacle.getBase_x() + i and int(self._base_y) - 1 == obstacle.getBase_y() + j or int(self._base_x) + 1 == obstacle.getBase_x() + i and int(self._base_y) - 1 == obstacle.getBase_y() + j or int(self._base_x) == obstacle.getBase_x() + i and int(self._base_y) - 2 == obstacle.getBase_y() + j:
			obstacle.collision(screen, self)
			return 1
		return 0

	def firebeamsCollisionCheck(self, firebeams, screen):
		for firebeam in firebeams:
			if firebeam.getActivated() is 1:
				for i in range(int(screen.getScreenheight() / 4)):
					if firebeam.getShape() is 0 and self.collisionCheck(screen, firebeam, -i, i) == 1:
						break
					elif firebeam.getShape() is 1 and self.collisionCheck(screen, firebeam, 0, i) == 1:
						break
					elif firebeam.getShape() is 2 and self.collisionCheck(screen, firebeam, i, i) == 1:
						break
					elif firebeam.getShape() is 3 and self.collisionCheck(screen, firebeam, i, 0) == 1:
						break

	def coinsCollisionCheck(self, coins, screen):
		for coin in coins:
			if coin.getActivated() is 1 and self.collisionCheck(screen, coin, 0, 0) == 1:
				break

	def move(self, screen, firebeams, coins, character, refresh_rate):
		self.removeHero(screen)
		if self._shield == 1 and time.time() - self._shield_time > self._shield_recharge_time:
			self.deactivateShield()
		if character in ["w", "W"]:
			self._y_velocity -= 1 / refresh_rate
		else:
			self._y_velocity += 1 / refresh_rate
			if character in ["a", "A"]:
				self._base_x -= self._x_velocity
			elif character in ["d", "D"]:
				self._base_x += self._x_velocity
			elif character in [" "] and time.time() - self._shield_time > self._shield_on_time:
				self._shield_time = time.time()
				self.activateShield()
		if self._base_x < screen.getStart() + 1:
			self._base_x = screen.getStart() + 1
		elif self._base_x > screen.getStart() + screen.getScreenwidth() - 3:
			self._base_x = screen.getStart() + screen.getScreenwidth() - 3
		self.firebeamsCollisionCheck(firebeams, screen)
		self.coinsCollisionCheck(coins, screen)
		self._base_y += self._y_velocity
		if self._base_y < 2:
			self._base_y = 2
			self._y_velocity = 0
		elif self._base_y > screen.getScreenheight() - 1:
			self._base_y = screen.getScreenheight() - 1
			self._y_velocity = 0
		self.firebeamsCollisionCheck(firebeams, screen)
		self.coinsCollisionCheck(coins, screen)
		self.placeHero(screen)
		return

	def shoot(self):
		pass
