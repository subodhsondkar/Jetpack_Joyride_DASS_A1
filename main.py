import time
from screen import Screen
from player import Hero, Player
from obstacle import Firebeam, Coin, Magnet
from initialisations import initialiseFirebeams, initialiseCoins, initialiseMagnets
from input import Get, input_to

'''
To Do List:

Magnet: configuring x_velocity and back to normal when magnet is no longer present
Boss enemy (dragon): his bullet is an ice ball. More hai
Game end
'''

total_time = 30
refresh_time = 0.05
screen = Screen(250)
firebeams = initialiseFirebeams(screen)
coins = initialiseCoins(screen)
magnets = initialiseMagnets(screen)
bullets = []
mandalorian = Player(screen, screen.getScreenwidth() / 4, screen.getScreenheight() - 1, refresh_time)
screen.printScreen(mandalorian, total_time)
get = Get()
input_taken = 0
start_time = time.time()
previous_time = start_time
times = []
z = 0
while True:
	current_time = time.time()
	time_remaining = total_time - time.time() + start_time
	if time_remaining < 0:
		mandalorian.gameOver()
	if current_time - previous_time >= refresh_time:
		print( "\033[0;0H" )
		if screen.getStart() < screen.getGamewidth() - screen.getScreenwidth() + 2:
			screen.incrementStart()
		screen.printScreen(mandalorian, time_remaining)
		previous_time = time.time()
		input_taken = 0
	input = input_to(get, refresh_time)
	if input == None:
		input = ""
	if input_taken == 0:
		times += [-time.time()]
		refresh_time = mandalorian.move(screen, firebeams, coins, magnets, bullets, input, refresh_time)
		times[z] += time.time()
		z += 1
		input_taken = 1
