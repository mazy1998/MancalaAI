# Mancal AI

## Install
To launch this application make sure you are in a Python 3.x environment with p5 package installed.

1. Installing Python 3.x
2. Follow the installation guide for [p5]
3. Clone the Repository
4. Play Mancala

## Mancala Rules
Mancala is a two player game in which the players have to move the stones on the board and try to capture as many stones they can in their tray. The player that has the most stones in their tray at the end of the game wins. 

There exist many variations of the game and our implementation is based on the rules defined [here](https://www.coolmathgames.com/0-mancala)

## Setup
There are 12 slots on the board, with 4 pebbles in each at the initial state of the game. The two player trays at each end are initially empty, with the tray on the right side belonging to Player 1 and the tray on the left belonging to AI/Player 2.

## Playing
The game starts by showing the following screen to the user

![Splash Screen](https://raw.githubusercontent.com/mazy1998/MancalaAI/master/scr2.png)
    
There are two modes available
- 2 Player Mode: Play against another human
-  AI Mode: Play against our AI

This is the initial game state

![Splash Screen](https://raw.githubusercontent.com/mazy1998/MancalaAI/master/scr1.png)

## Algorithms
- Minimax with Alpha-Beta Pruning
- Alpha Beta Pruning
 - Neural Networks

[p5]: <https://p5.readthedocs.io/en/latest/install.html>
[splash]: <https://raw.githubusercontent.com/mazy1998/MancalaAI/master/scr1.png>
