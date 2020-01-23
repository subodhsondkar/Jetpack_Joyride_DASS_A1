class Bullet():
	def __init__(self, player, refresh_time, direction):
		self._base_x = player.getBase_x() + 2 * direction
		self._base_y = player.getBase_y() - 1
		self._velocity_x = 5 * direction / refresh_time
		self._velocity_y = 0
		self._direction = direction
		self._activated = 1
		return

	def getBase_x(self):
		return self._base_x

	def getBase_y(self):
		return self._base_y

	def getActivated(self):
		return self._activated

	def deactivateBullet(self, screen, i, j):
		screen.setGame(int(self._base_y) + j, int(self._base_x) + i, "H")
		self._activated = 0

	def move(self, screen, firebeams, coins, magnets, player, refresh_time):
		screen.setGame(int(self._base_y), int(self._base_x), "H")
		#if self._direction == 1:
		if True:
			dead_bullet = 0
			for i in range(int(self._velocity_x * refresh_time) + 1):
				for j in range(int(self._velocity_y * refresh_time) + 1):
					for coin in coins:
						if coin.getActivated() == 1 and int(self._base_x) + i * self._direction + 1 == coin.getBase_x() and int(self._base_y) + j == coin.getBase_y():
							coin.collision(screen, player, 0)
							self.deactivateBullet(screen, i * self._direction, j)
							dead_bullet = 1
					for magnet in magnets:
						if magnet.getActivated() == 1 and int(self._base_x) + i * self._direction + 1 == magnet.getBase_x() and int(self._base_y) + j == magnet.getBase_y():
							magnet.collision(screen, player, 0)
							self.deactivateBullet(screen, i * self._direction, j)
							dead_bullet = 1
					for firebeam in firebeams:
						if firebeam.getActivated() == 1:
							for k in range(int(screen.getScreenheight() / 4)):
								if firebeam.getShape() == 0 and int(self._base_x) + i * self._direction + 1 == firebeam.getBase_x() - k and int(self._base_y) + j == firebeam.getBase_y() + k:
									firebeam.collision(screen, player, 0)
									self.deactivateBullet(screen, i * self._direction, j)
									dead_bullet = 1
									break
								elif firebeam.getShape() == 1 and int(self._base_x) + i * self._direction + 1 == firebeam.getBase_x() and int(self._base_y) + j == firebeam.getBase_y() + k:
									firebeam.collision(screen, player, 0)
									self.deactivateBullet(screen, i * self._direction, j)
									dead_bullet = 1
									break
								elif firebeam.getShape() == 2 and int(self._base_x) + i * self._direction + 1 == firebeam.getBase_x() + k and int(self._base_y) + j == firebeam.getBase_y() + k:
									firebeam.collision(screen, player, 0)
									self.deactivateBullet(screen, i * self._direction, j)
									dead_bullet = 1
									break
								elif firebeam.getShape() == 3 and int(self._base_x) + i * self._direction + 1 == firebeam.getBase_x() + k and int(self._base_y) + j == firebeam.getBase_y():
									firebeam.collision(screen, player, 0)
									self.deactivateBullet(screen, i * self._direction, j)
									dead_bullet = 1
									break
			self._base_x += self._velocity_x * refresh_time
			if self._base_x > screen.getScreenwidth() + screen.getStart() - self._velocity_x * refresh_time - 3 or self._base_x < 0 or self._base_y > screen.getScreenheight() - 1 or self._base_y < 0:
				self.deactivateBullet(screen, 0, 0)
			elif dead_bullet == 0:
				screen.setGame(int(self._base_y), int(self._base_x), "B")
		else:
			pass
		return
