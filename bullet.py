class Bullet():
	def __init__(self, hero):
		self._base_x = hero.getBase_x() + 1
		self._base_y = hero.getBase_y() - 1
		self._velocity_x = 3
		self._velocity_y = 0
