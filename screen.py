import os
from colorama import Back, Fore
import numpy as np

'''
Mapping:

H: hawa
F: firebeam
["O ", "|<", "^ "]: hero
C: coin
M: magnet
E: enemy
B: bullet
'''
mapping = {
	"H": Back.WHITE,
	"F": Back.RED,
	"C": Back.YELLOW,
}

class Screen():
	def __init__(self, gamewidth):
		self.__screenheight, self.__screenwidth = os.popen("stty size", "r").read().split()
		self.__screenheight = int(self.__screenheight) - 8
		self.__screenwidth = int(self.__screenwidth) - 2
		self.__gamewidth = gamewidth
		self.__game = []
		self.__start = 0
		for i in range(self.__screenheight):
			current_row = []
			for j in range(self.__gamewidth):
				current_row += ["H"]
			self.__game += [current_row]
		self.__game = np.asarray(self.__game)
		return

	def getScreenheight(self):
		return self.__screenheight

	def getScreenwidth(self):
		return self.__screenwidth

	def getGamewidth(self):
		return self.__gamewidth

	def getGame(self):
		return self.__game

	def getStart(self):
		return self.__start

	def setGame(self, i, j, new_character):
		self.__game[i][j] = new_character
		return

	def incrementStart(self):
		self.__start += 1
		return

	def printScreen(self, hero, time_remaining):
		for i in range(self.__screenwidth + 2):
			print(Back.BLACK + " ", end = "")
		print(Back.WHITE)
		print_string = " SCORE: " + str(hero.getScore()) + " | LIVES: " + str(hero.getLives()) + " | TIME REMAINING: " + str(int(time_remaining))
		print(Back.BLACK + Fore.WHITE + print_string, end = "")
		for i in range(self.__screenwidth + 2 - len(print_string)):
			print(Back.BLACK + " ", end = "")
		print(Back.WHITE)
		for i in range(self.__screenwidth + 2):
			print(Back.BLACK + " ", end = "")
		print(Back.WHITE)
		for i in range(self.__screenwidth + 2):
			print(Back.BLACK + " ", end = "")
		print(Back.WHITE)
		for i in range(2):
			print(Back.BLACK + "  ", end = "")
			for j in range(self.__screenwidth - 2):
				print(Back.BLUE + " ", end = "")
			print(Back.BLACK + "  ", end = "")
			print(Back.WHITE)
		for i in range(self.__screenheight):
			print(Back.BLACK + "  ", end = "")
			for j in range(self.__screenwidth - 2):
				try:
					print(mapping[self.__game[i][j + self.__start]] + " ", end = "")
				except:
					if hero.getShield() == 0:
						print(Back.WHITE + Fore.BLACK + self.__game[i][j + self.__start], end = "")
					else:
						print(Back.RED + Fore.BLACK + self.__game[i][j + self.__start], end = "")						
			print(Back.BLACK + "  ", end = "")
			print(Back.WHITE)
		for i in range(2):
			print(Back.BLACK + "  ", end = "")
			for j in range(self.__screenwidth - 2):
				print(Back.GREEN + " ", end = "")
			print(Back.BLACK + "  ", end = "")
			print(Back.WHITE)
		for i in range(self.__screenwidth + 2):
			print(Back.BLACK + " ", end = "")
		print(Back.WHITE)
		return
