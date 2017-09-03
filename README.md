

# Startcraft Pysc2 Deepmind minigames creation
This repository aims to serve as a guide for opensource contributing in minigame pysc2 library for Artificial Intelligence reserach.
From Deepmind pysc2 paper you can find the following minigame description
For minigame execution you should go to https://github.com/deepmind/pysc2 and install requirements

## Minigame task description
To investigate elements of the game in isolation, and to provide further fine-grained steps towards playing the full game, we built several mini-games. These are focused scenarios on small maps that have been constructed with the purpose of testing a subset of actions and/or game mechanics with a clear reward structure. Unlike the full game where the reward is just win/lose/tie, the reward structure for mini-games can reward particular behaviours (as defined in a corresponding .SC2Map file).

## Minigame introduction
Before creating a minigame, I encourage you to run the alredy developed ones to see wich task are subdivided into each minigame as the design could be important . The minigame title gives us a description of the goal 
Find bellow the exploration of DefeatRoaches mini-game map 

Execute in your terminal 
'''$ python3 -m pysc2.bin.agent --map DefeatRoaches '''

![alt tag] https://github.com/SoyGema/Startcraft/blob/master/Images/Captura%20de%20pantalla%202017-09-03%20a%20las%2012.05.18.png

This is a human interpretable view of the game on the left, and coloured versions of the feature layers on the right. Find in top left described the actions 
Attack
Stop
Move
MovePatrol
MoveHoldPosition
Green circles are used to define player1(terran) and red circles correspond to player2(roaches)

Startcraft dataset and AI research 
## Useful resources about Startcraft 
DeepMind paper

DataSet exploration
https://arxiv.org/pdf/1708.02139.pdf
Pysc2 deepmind reserach paper

Link to Pysc2 repository 
