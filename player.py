import time
from bullet import Bullet

def signum(var):
	if var < 0: return -1
	elif var > 0: return 1
	else: return 0

class Player():
	def __init__(self, x, y):
		self._base_x = x
		self._base_y = y
		self._lives = 3
		return

	def getBase_x(self):
		return self._base_x

	def getBase_y(self):
		return self._base_y

	def getLives(self):
		return self._lives

	def killed(self, player):
		if self._shield == 1:
			return
		else:
			self._lives -= 1
			if self._lives == 0:
				self.gameOver(player)
		return

	def gameOver(self, player):
		print("Score:", player._score, "| Lives:", player._lives)
		input("Press enter key to continue.")
		exit()

class Enemy(Player):
	def __init__(self, screen, x, y):
		super().__init__(x, y)
		self._shield = 0
		self._shoot_off_time = 1
		self._shoot_time = time.time() - self._shoot_off_time
		self.placePlayer(screen)
		return

	def removePlayer(self, screen):
		screen.setGame(int(self._base_y) - 2, int(self._base_x), "H")
		screen.setGame(int(self._base_y) - 1, int(self._base_x), "H")
		screen.setGame(int(self._base_y) - 1, int(self._base_x) - 1, "H")
		screen.setGame(int(self._base_y), int(self._base_x), "H")
		return

	def placePlayer(self, screen):
		screen.setGame(int(self._base_y) - 2, int(self._base_x), "O")
		screen.setGame(int(self._base_y) - 1, int(self._base_x), "|")
		screen.setGame(int(self._base_y) - 1, int(self._base_x) - 1, ">")
		screen.setGame(int(self._base_y), int(self._base_x), "^")
		return

	def move(self, screen, hero, refresh_time, bullets):
		if time.time() - self._shoot_time > self._shoot_off_time:
			bullets += [Bullet(self, refresh_time, -1)]
			self._shoot_time = time.time()
		self.removePlayer(screen)
		self._base_y = hero.getBase_y()
		self.placePlayer(screen)
		return

class Hero(Player):
	def __init__(self, screen, x, y, refresh_time):
		super().__init__(x, y)
		self._velocity_y = 0
		self._acceleration_y = 3 / refresh_time
		self._score = 0
		self._shield = 0
		self._shield_on_time = 5
		self._shield_recharge_time = 10
		self._shield_time = time.time() - self._shield_recharge_time
		self._speed_boost = 1
		self._speed_boost_on_time = 5
		self._speed_boost_time = time.time()
		self.placePlayer(screen)
		return

	def getScore(self):
		return self._score

	def getShield(self):
		return self._shield

	def getSpeed_boost(self):
		return self._speed_boost

	def activateShield(self):
		self._shield = 1
		return

	def deactivateShield(self):
		self._shield = 0
		return

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
			obstacle.collision(screen, self, 1)
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

	def magnetsEffect(self, magnets, refresh_time):
		for magnet in magnets:
			if magnet.getActivated() == 1 and (self._base_x - magnet.getBase_x()) ** 2 + (self._base_y - magnet.getBase_y()) ** 2 <= 200:
				self._velocity_y += signum(magnet.getBase_y() - self._base_y + 1)
				self._base_x += signum(magnet.getBase_x() - self._base_x) * magnet.getOn_time() * 0.05
				magnet.enter()
			else:
				magnet.exit()

	def move(self, screen, enemy, firebeams, coins, magnets, bullets, character, refresh_time):
		self.removePlayer(screen)
		if self._shield == 1 and time.time() - self._shield_time > self._shield_on_time:
			self.deactivateShield()
		if self._speed_boost == 2 and time.time() - self._speed_boost_time > self._speed_boost_on_time:
			self._speed_boost = 1
			refresh_time /= 2
		if character in ["q", "Q"]:
			self.gameOver()
		elif character in ["w", "W"]:
			self._velocity_y -= self._acceleration_y * refresh_time * self._speed_boost
		else:
			self._velocity_y += self._speed_boost
			if character in ["a", "A"]:
				self._base_x -= 2 * self._speed_boost
			elif character in ["d", "D"]:
				self._base_x += 2 * self._speed_boost
			elif character in ["s", "S"]:
				bullets += [Bullet(self, refresh_time, 1)]
			elif character in ["p", "P"] and self._speed_boost == 1:
				self._speed_boost_time = time.time()
				self._speed_boost = 2
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
		self._base_y += self._velocity_y * refresh_time * self._speed_boost
		if self._base_y < 2:
			self._base_y = 2
			self._velocity_y = 0
		elif self._base_y > screen.getScreenheight() - 1:
			self._base_y = screen.getScreenheight() - 1
			self._velocity_y = 0
		self.firebeamsCollisionCheck(firebeams, screen)
		self.coinsCollisionCheck(coins, screen)
		self.magnetsCollisionCheck(magnets, screen)
		self.magnetsEffect(magnets, refresh_time)
		if self._base_x < screen.getStart() + 1:
			self._base_x = screen.getStart() + 1
		elif self._base_x > screen.getStart() + screen.getScreenwidth() - 4:
			self._base_x = screen.getStart() + screen.getScreenwidth() - 4
		if self._base_y < 2:
			self._base_y = 2
			self._velocity_y = 0
		elif self._base_y > screen.getScreenheight() - 1:
			self._base_y = screen.getScreenheight() - 1
			self._velocity_y = 0
		self.placePlayer(screen)
		enemy.move(screen, self, refresh_time, bullets)
		for bullet in bullets:
			if bullet.getActivated() == 1:
				bullet.move(screen, firebeams, coins, magnets, self, enemy, refresh_time)
		return
