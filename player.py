import time
from bullet import Bullet

class Player():
	def __init__(self, screen, x, y, refresh_time):
		self._base_x = x
		self._base_y = y
		self._velocity_x = 2 / refresh_time
		self._velocity_y = 0
		self._acceleration_y = 3
		self._lives = 3
		self._score = 0
		self._shield = 0
		self._shield_on_time = 5
		self._shield_recharge_time = 10
		self._shield_time = time.time() - self._shield_recharge_time
		self._speed_boost = 0
		self._speed_boost_on_time = 5
		self._speed_boost_time = time.time()
		self.placePlayer(screen)
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
		if self._shield == 1:
			return
		else:
			self._lives -= 1
			if self._lives == 0:
				self.gameOver()
		return

	def gameOver(self):
		print("Score:", self._score, "| Lives:", self._lives)
		input("Press enter key to continue.")
		exit()

	def incrementPoints(self, points):
		self._score += points
		return

	def removePlayer(self, screen):
		screen.setGame(int(self._base_y) - 2, int(self._base_x), "H")
		screen.setGame(int(self._base_y) - 1, int(self._base_x), "H")
		screen.setGame(int(self._base_y) - 1, int(self._base_x) + 1, "H")
		screen.setGame(int(self._base_y), int(self._base_x), "H")
		return

	def placePlayer(self, screen):
		screen.setGame(int(self._base_y) - 2, int(self._base_x), "O")
		screen.setGame(int(self._base_y) - 1, int(self._base_x), "|")
		screen.setGame(int(self._base_y) - 1, int(self._base_x) + 1, "<")
		screen.setGame(int(self._base_y), int(self._base_x), "^")
		return

	def collisionCheck(self, screen, obstacle, i, j):
		if int(self._base_x) == obstacle.getBase_x() + i and int(self._base_y) == obstacle.getBase_y() + j or int(self._base_x) == obstacle.getBase_x() + i and int(self._base_y) - 1 == obstacle.getBase_y() + j or int(self._base_x) == obstacle.getBase_x() + i and int(self._base_y) - 2 == obstacle.getBase_y() + j or int(self._base_x) + 1 == obstacle.getBase_x() + i and int(self._base_y) == obstacle.getBase_y() + j or int(self._base_x) + 1 == obstacle.getBase_x() + i and int(self._base_y) - 1 == obstacle.getBase_y() + j or int(self._base_x) + 1 == obstacle.getBase_x() + i and int(self._base_y) - 2 == obstacle.getBase_y() + j:
			obstacle.collision(screen, self)
			return 1
		return 0

	def firebeamsCollisionCheck(self, firebeams, screen):
		for firebeam in firebeams:
			if firebeam.getActivated() == 1:
				for i in range(int(screen.getScreenheight() / 4)):
					if firebeam.getShape() == 0 and self.collisionCheck(screen, firebeam, -i, i) == 1:
						break
					elif firebeam.getShape() == 1 and self.collisionCheck(screen, firebeam, 0, i) == 1:
						break
					elif firebeam.getShape() == 2 and self.collisionCheck(screen, firebeam, i, i) == 1:
						break
					elif firebeam.getShape() == 3 and self.collisionCheck(screen, firebeam, i, 0) == 1:
						break
		return

	def coinsCollisionCheck(self, coins, screen):
		for coin in coins:
			if coin.getActivated() == 1 and self.collisionCheck(screen, coin, 0, 0) == 1:
				break
		return

	def magnetsCollisionCheck(self, magnets, screen):
		for magnet in magnets:
			if magnet.getActivated() == 1 and self.collisionCheck(screen, magnet, 0, 0) == 1:
				break
		return

	def move(self, screen, firebeams, coins, magnets, bullets, character, refresh_time):
		self.removePlayer(screen)
		if self._shield == 1 and time.time() - self._shield_time > self._shield_on_time:
			self.deactivateShield()
		if self._speed_boost == 1 and time.time() - self._speed_boost_time > self._speed_boost_on_time:
			self._speed_boost = 0
			refresh_time /= 2
		if character in ["w", "W"]:
			self._velocity_y -= self._acceleration_y * refresh_time
		else:
			self._velocity_y += refresh_time
			if character in ["a", "A"]:
				self._base_x -= self._velocity_x * refresh_time
			elif character in ["d", "D"]:
				self._base_x += self._velocity_x * refresh_time
			elif character in ["s", "S"]:
				bullets += [Bullet(self, refresh_time)]
			elif character in ["p", "P"] and self._speed_boost == 0:
				self._speed_boost_time = time.time()
				self._speed_boost = 1
				refresh_time *= 2
			elif character in [" "] and time.time() - self._shield_time > self._shield_recharge_time:
				self._shield_time = time.time()
				self.activateShield()
		if self._base_x < screen.getStart() + 1:
			self._base_x = screen.getStart() + 1
		elif self._base_x > screen.getStart() + screen.getScreenwidth() - 4:
			self._base_x = screen.getStart() + screen.getScreenwidth() - 4
		self.firebeamsCollisionCheck(firebeams, screen)
		self.coinsCollisionCheck(coins, screen)
		self.magnetsCollisionCheck(magnets, screen)
		self._base_y += self._velocity_y
		if self._base_y < 2:
			self._base_y = 2
			self._velocity_y = 0
		elif self._base_y > screen.getScreenheight() - 1:
			self._base_y = screen.getScreenheight() - 1
			self._velocity_y = 0
		self.firebeamsCollisionCheck(firebeams, screen)
		self.coinsCollisionCheck(coins, screen)
		self.magnetsCollisionCheck(magnets, screen)
		self.placePlayer(screen)
		for bullet in bullets:
			if bullet.getActivated() == 1:
				bullet.move(screen, firebeams, coins, magnets, self, refresh_time)
		return refresh_time

class Hero(Player):
	def __init__(self, screen, x, y, refresh_time):
		pass		

class Enemy(Player):
	def __init__(self, screen):
		pass
