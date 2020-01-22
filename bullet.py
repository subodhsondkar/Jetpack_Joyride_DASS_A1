class Bullet():
	def __init__(self, hero, refresh_time):
		self._base_x = hero.getBase_x() + 2
		self._base_y = hero.getBase_y() - 1
		self._velocity_x = 5 / refresh_time
		#self._velocity_y = 0
		self._activated = 1
		return

	def getBase_x(self):
		return self._base_x

	def getBase_y(self):
		return self._base_y

	def getActivated(self):
		return self._activated

	def deactivateBullet(self, screen):
		screen.setGame(int(self._base_y), int(self._base_x), "H")
		self._activated = 0
		return

	'''def move(self, screen, firebeams, coins, refresh_time):
		screen.setGame(int(self._base_y), int(self._base_x), "H")
		for i in range(int(self._velocity_x * refresh_time) + 1):
			for j in range(int(self._velocity_y * refresh_time) + 1):
				for coin in coins:
					if coin.getActivated() is 1 and int(self._base_x) + i is coin.getBase_x() and int(self._base_y) + j is coin.getBase_y():
						coin.deactivateObstacle(screen)
						self.deactivateBullet()
				for firebeam in firebeams:
					if firebeam.getActivated() is 1:
						for k in range(int(screen.getScreenheight() / 4)):
							if firebeam.getShape() is 0 and int(self._base_x) + i is firebeam.getBase_x() - k and int(self._base_y) + j is firebeam.getBase_y() + k:
								firebeam.deactivateObstacle(screen)
								self.deactivateBullet()
								break
							elif firebeam.getShape() is 1 and int(self._base_x) + i is firebeam.getBase_x() and int(self._base_y) + j is firebeam.getBase_y() + k:
								firebeam.deactivateObstacle(screen)
								self.deactivateBullet()
								break
							elif firebeam.getShape() is 2 and int(self._base_x) + i is firebeam.getBase_x() + k and int(self._base_y) + j is firebeam.getBase_y() + k:
								firebeam.deactivateObstacle(screen)
								self.deactivateBullet()
								break
							elif firebeam.getShape() is 3 and int(self._base_x) + i is firebeam.getBase_x() + k and int(self._base_y) + j is firebeam.getBase_y():
								firebeam.deactivateObstacle(screen)
								self.deactivateBullet()
								break
		self._base_x += self._velocity_x * refresh_time
		self._base_y += self._velocity_y * refresh_time
		if self._base_x > screen.getScreenwidth() + screen.getStart() - 3 or self._base_x < 0 or self._base_y > screen.getScreenheight() - 1 or self._base_y < 0:
			self.deactivateBullet()
		else:
			screen.setGame(int(self._base_y), int(self._base_x), "B")
		return'''

	def move(self, screen, firebeams, coins, refresh_time):
		screen.setGame(int(self._base_y), int(self._base_x), "H")
		dead_bullet = 0
		for i in range(int(self._velocity_x * refresh_time)):
			for coin in coins:
				if coin.getActivated() is 1 and int(self._base_x) + i + 1 is coin.getBase_x() and int(self._base_y) is coin.getBase_y():
					coin.deactivateObstacle(screen)
					self.deactivateBullet(screen)
					dead_bullet = 1
			for firebeam in firebeams:
				if firebeam.getActivated() is 1:
					for k in range(int(screen.getScreenheight() / 4)):
						if firebeam.getShape() is 0 and int(self._base_x) + i is firebeam.getBase_x() - k and int(self._base_y) is firebeam.getBase_y() + k:
							firebeam.deactivateObstacle(screen)
							self.deactivateBullet(screen)
							dead_bullet = 1
							break
						elif firebeam.getShape() is 1 and int(self._base_x) + i is firebeam.getBase_x() and int(self._base_y) is firebeam.getBase_y() + k:
							firebeam.deactivateObstacle(screen)
							self.deactivateBullet(screen)
							dead_bullet = 1
							break
						elif firebeam.getShape() is 2 and int(self._base_x) + i is firebeam.getBase_x() + k and int(self._base_y) is firebeam.getBase_y() + k:
							firebeam.deactivateObstacle(screen)
							self.deactivateBullet(screen)
							dead_bullet = 1
							break
						elif firebeam.getShape() is 3 and int(self._base_x) + i is firebeam.getBase_x() + k and int(self._base_y) is firebeam.getBase_y():
							firebeam.deactivateObstacle(screen)
							self.deactivateBullet(screen)
							dead_bullet = 1
							break
		self._base_x += self._velocity_x * refresh_time
		if self._base_x > screen.getScreenwidth() + screen.getStart() - self._velocity_x * refresh_time - 3 or self._base_x < 0 or self._base_y > screen.getScreenheight() - 1 or self._base_y < 0:
			self.deactivateBullet(screen)
		elif dead_bullet == 0:
			screen.setGame(int(self._base_y), int(self._base_x), "B")
		return
