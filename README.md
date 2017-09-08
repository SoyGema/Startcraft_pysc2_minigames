

# Startcraft Pysc2 Deepmind minigames creation
This repository aims to serve as a guide for opensource contributing in minigame pysc2 library for Artificial Intelligence reserach.

For minigame instalation for execution you should go to https://github.com/deepmind/pysc2 and install requirements

## Minigame task description
Minigames come as a controled environments that might be useful to exploit game features in SC2. General purpose learning system for Startcraft 2 can be a daunting task. So there is a logical option in splitting this tasks into minitask in orther to advance in research . 
To investigate elements of the game in isolation, and to provide further fine-grained steps towards playing the full game, Deepmind has  built several mini-games. These are focused scenarios on small maps that have been constructed with the purpose of testing a subset of actions and/or game mechanics with a clear reward structure. Unlike the full game where the reward is just win/lose/tie, the reward structure for mini-games can reward particular behaviours (as defined in a corresponding .SC2Map file).

## Minigame introduction
Before creating a minigame, I encourage you to run the alredy developed ones to see wich task are subdivided into each minigame as the design could be important . The minigame title gives us a description of the goal 
Find bellow the exploration of DefeatRoaches mini-game map 


## DefeatRoaches

#### Description

A map with 9 Marines and a group of 4 Roaches on opposite sides. Rewards are earned by using the Marines to defeat Roaches, with optimal combat strategy requiring the Marines to perform focus fire on the Roaches. Whenever all 4 Roaches have been defeated, a new group of 4 Roaches is spawned and the player is awarded 5 additional Marines at full health, with all other surviving Marines retaining their existing health (no restore). Whenever new units are spawned, all unit positions are reset to opposite sides of the map.

#### Initial State

*   9 Marines in a vertical line at a random side of the map (preselected)
*   4 Roaches in a vertical line at the opposite side of the map from the
    Marines

#### Rewards

*   Roach defeated: +10
*   Marine defeated: -1

#### End Conditions

*   Time elapsed
*   All Marines defeated

#### Time Limit

*   120 seconds

![alt tag](https://github.com/SoyGema/Startcraft/blob/master/Images/Captura%20de%20pantalla%202017-09-03%20a%20las%2012.05.18.png)

This is a human interpretable view of the game on the left, and coloured versions of the feature layers on the right. Find in top left described the actions 
a-Attack
d-Stop
m-Move
p-MovePatrol
t-MoveHoldPosition
Green circles are used to define player1(terran) and red circles correspond to player2(roaches)


#### Defeat Roaches analysis

Two different type of agents have been executed in this minimap. As a matter of results, you can find bellow listed the difference in between them 

#### Experiment 1

DefeatRoaches minigame map random agent
```shell
$ python3 -m pysc2.bin.agent --map DefeatRoaches
```
watch video at 
[![MarinesVSRoaches](https://github.com/SoyGema/Startcraft/blob/master/Images/2C01EB1027814BB7FF16A15272E1B2DEF9FDEEC3.jpg)](https://www.youtube.com/watch?v=tYxleQHgWJE "Random Agent MarinesVS Roaches")

*   Priorization of moving in map (marine player 1) VS attack (roaches player 2) 
*   Playing for 15min with all defeats for player 1 
*   Note that this is not a scripted agent. 
*   The game was executing during 15 minutes approximately 
*   Find bellow the 17 actions the agent was actually executing during the game 
![alt tag](https://github.com/SoyGema/Startcraft/blob/master/Images/print_screen_1.png)

#### Experiment 2 

DefeatRoaches minigame map scripted agent 
```shell
$ python3 -m pysc2.bin.agent --map DefeatRoaches --agent pysc2.agents.scripted_agent.DefeatRoaches
```
watch video at 
[![MarinesVSRoaches](https://github.com/SoyGema/Startcraft/blob/master/Images/2C01EB1027814BB7FF16A15272E1B2DEF9FDEEC3.jpg)](https://www.youtube.com/watch?v=XvYWLRBf-5U "Scripted Agent MarinesVS Roaches")

*   No map random exploration by agent
*   Increased number of victories by agent 
*   However, there seems to be a balance in between . 
*   In the middle of the game you can see player 1 is currently winning and the agent starts losing as it imbalance by rules games. 
*   Everytime the game is executed it shows an error at aproximately min 15 
*  Error has been reported to blizzard team 

Startcraft dataset and AI research 
## Useful resources about Startcraft 
DeepMind paper

DataSet exploration
https://arxiv.org/pdf/1708.02139.pdf
Pysc2 deepmind reserach paper

Link to Pysc2 repository 
https://github.com/deepmind/pysc2
