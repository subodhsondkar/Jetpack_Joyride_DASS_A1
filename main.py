import time
from screen import Screen
from hero import Hero
from obstacle import Firebeam, Coin, Magnet
from bullet import Bullet
from initialisations import initialiseFirebeams, initialiseCoins
from input import Get, input_to

'''
To Do List:

OOPS: just check once
Bullet: shooting firebeam, coins, magnets, boss enemy
Magnet: configuring x_velocity and back to normal when magnet is no longer present
Speed boost: what is combined effect of magnet and speed boost
Boss enemy (dragon): his bullet is an ice ball. More hai
Game end
BONUS dragon
'''

total_time = 20
refresh_time = 0.05
screen = Screen(250)
firebeams = initialiseFirebeams(screen)
coins = initialiseCoins(screen)
mandalorian = Hero(screen, screen.getScreenwidth() / 4, screen.getScreenheight() - 1)
screen.printScreen(mandalorian, total_time)
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
		if screen.getStart() < screen.getGamewidth() - screen.getScreenwidth() + 2:
			screen.incrementStart()
		screen.printScreen(mandalorian, time_remaining)
		previous_time = time.time()
		input_taken = 0
	input = input_to(get, refresh_time)
	if input is None:
		input = ""
	if input_taken == 0:
		mandalorian.move(screen, firebeams, coins, input, refresh_time)
		input_taken = 1
