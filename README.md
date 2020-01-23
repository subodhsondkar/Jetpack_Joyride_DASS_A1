# Jetpack Joyride

## Objective
The game must simulate a basic version the infamous mobile game Jetpack Joyride. We need to defeat the boss before the time runs out. The objective of the game is to get the most points by collecting coins and destroying obstacles before killing the boss.

## Playing The Game
```
python3 main.py
```

## Features
- The game is implemented in python3.
- The code is modular and follows OOPS.
- Uses core python3 packages and colorama library.
- Player can move left or right, accelerate upwards, shoot bullets, or use the shield.
- You get killed on coming in contact with a firebeam.
- You get points on collect coins, or shooting at obstacles.
- You can shoot the firebeam to deactivate it.
- Colours are implemented using colorama library.

## Controls
- "a" or "A": move towards the left.
- "d" or "D": move towards the right.
- "w" or "W": accelerate upwards.
- "s" or "S": shoot bullets.
- "p" or "P": activate speed booster.
- " " (SPACE): activate shield.
- "q" or "Q": quit the game.

## OOPS
### Inheritance
- Hero, and Enemy classes inherit from Player class.
- Firebeam, Coin, and Magnet classes inherit from Obstacle class.
### Polymorphism
- placeObstacle(), and collision() are functions which have different definitions for Firebeam, Coin, and Magnet classes.
- removePlayer(), placePlayer(), and move() functions which have different definitions for Hero and Enemy classes.
### Encapsulation
- Class and object based approach for all the functionality has been implemented.
### Abstraction
- Properties of every class are hidden from the user using abstaction and are accessed and edited using getter and setter functions.

## Obstacles
There are three types of obstacles:
- Firebeam
- Coin
- Magnet

## Background and Scenery
- The scenery and the obstacles must change as you move in and out of the window. There is a platform and a sky. The Mandalorian can't go below the platform or above the sky. There are a lot of coins suspended in the air which can be collected by the Mandalorian.

## Score
The final score is calculated as :
```
score = 10 * coin_collect + 2 * magnet_collect + 5 * magnet_shot + 16 * firebeam_hit
```

## Boss Enemy
- The boss enemy can adjust his position according to the Mandalorian and shoots bullets aimed at the Mandalorian.
