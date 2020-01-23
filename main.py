import time
from screen import Screen
from player import Player
from obstacle import Firebeam, Coin, Magnet
from initialisations import initialiseFirebeams, initialiseCoins, initialiseMagnets
from input import Get, input_to

'''
To Do List:

Boss enemy (dragon): his bullet is an ice ball. More hai
Game end
'''

total_time = 45
refresh_time = 0.05
screen = Screen(400)
mandalorian = Player(screen, screen.getScreenwidth() / 4, screen.getScreenheight() - 1, refresh_time)
firebeams = initialiseFirebeams(screen)
coins = initialiseCoins(screen)
magnets = initialiseMagnets(screen)
bullets = []
get = Get()
input_taken = 0
start_time = time.time()
previous_time = start_time
while True:
	current_time = time.time()
	time_remaining = total_time - time.time() + start_time
	if time_remaining < 0:
		mandalorian.gameOver()
	if current_time - previous_time >= refresh_time:
		print( "\033[0;0H" )
		screen.printScreen(mandalorian, time_remaining)
		previous_time = time.time()
		input_taken = 0
	input = input_to(get, refresh_time)
	if input == None:
		input = ""
	if input_taken == 0:
		refresh_time = mandalorian.move(screen, firebeams, coins, magnets, bullets, input, refresh_time)
		input_taken = 1
