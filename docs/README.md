

# Startcraft Pysc2 Deepmind minigames creation
This file aims to serve as a guide for opensource contributing in minigame pysc2 library for Artificial Intelligence reserach. In this document we will execute and change the map 'DefeatRoaches' for a 'DefeatWhatever' or some minor changes you could do in the StarCraft II editor for designing our own mini-battle 

For minigame instalation for execution you should go to the official repository https://github.com/deepmind/pysc2 and install requirements

## Minigame task description
Minigames come as a controled environments that might be useful to exploit game features in SC2. General purpose learning system for Startcraft 2 can be a daunting task. So there is a logical option in splitting this tasks into minitask in orther to advance in research . 
To investigate elements of the game in isolation, and to provide further fine-grained steps towards playing the full game, Deepmind has  built several mini-games. These are focused scenarios on small maps that have been constructed with the purpose of testing a subset of actions and/or game mechanics with a clear reward structure. Unlike the full game where the reward is just win/lose/tie, the reward structure for mini-games can reward particular behaviours (as defined in a corresponding .SC2Map file).

## Minigame introduction
Before creating a minigame, I encourage you to run the alredy developed ones to see wich task are subdivided into each minigame as the design could be important . The minigame title gives us a description of the goal 
Find bellow the exploration of DefeatRoaches mini-game map 


## From DefeatRoaches to Defeat'Whatever'

#### Description

A map with 9 Marines and a group of 4 Roaches on opposite sides. Rewards are earned by using the Marines to defeat Roaches, with optimal combat strategy requiring the Marines to perform focus fire on the Roaches. Whenever all 4 Roaches have been defeated, a new group of 4 Roaches is spawned and the player is awarded 5 additional Marines at full health, with all other surviving Marines retaining their existing health (no restore). Whenever new units are spawned, all unit positions are reset to opposite sides of the map.

#### Initial State ---------> Transformation UNIT CHANGE

*   9 Marines in a vertical line at a random side of the map (preselected) -------> 9 sentry
*   4 Roaches in a vertical line at the opposite side of the map from the  -------> 4 zerlings
    Marines

#### Rewards --------------> Transformation REWARD SHAPPING

*   Roach defeated: +10 ---------> Zerlings defeated : +5 
*   Marine defeated: -1 ---------> Sentry defeated : -5 

#### End Conditions

*   Time elapsed
*   All Marines defeated ---------> Sentry 

#### Time Limit

*   120 seconds

![alt tag](https://github.com/SoyGema/Startcraft/blob/master/Images/Captura%20de%20pantalla%202017-09-03%20a%20las%2012.05.18.png )

This is a human interpretable view of the game on the left, and coloured versions of the feature layers on the right. Find in top left described the actions 
*a-Attack
*d-Stop
*m-Move
*p-MovePatrol
*t-MoveHoldPosition
Green circles are used to define player1(terran) and red circles correspond to player2(roaches)
This abstraction might be useful for CNN training 


## 1.  Defeat Roaches Test Map

Two different type of agents have been executed in this minimap. As a matter of results, you can find bellow listed the difference in between them 

#### Experiment 1

DefeatRoaches minigame map random agent
```shell
$ python3 -m pysc2.bin.agent --map DefeatRoaches
```
watch video at 
[![MarinesVSRoaches](https://github.com/SoyGema/Startcraft/blob/master/Images/2C01EB1027814BB7FF16A15272E1B2DEF9FDEEC3.jpg)](https://www.youtube.com/watch?v=tYxleQHgWJE "Random Agent MarinesVS Roaches" )

*   Priorization of moving in map (marine player 1) VS attack (roaches player 2) 
*   Playing for 15min with all defeats for player 1 
*   Note that this is not a scripted agent. 
*   The game was executing during 15 minutes approximately 
*   Find bellow the 17 actions the agent was actually executing during the game 
You can find a complete list of actions in this link https://github.com/deepmind/pysc2/blob/master/pysc2/lib/actions.py#L553 . Think that when you are defining your own minimap you should list of actions of units.
![alt tag](https://github.com/SoyGema/Startcraft/blob/master/Images/print_screen_1.png )

#### Experiment 2 

DefeatRoaches minigame map scripted agent 
```shell
$ python3 -m pysc2.bin.agent --map DefeatRoaches --agent pysc2.agents.scripted_agent.DefeatRoaches
```
watch video at 
[![MarinesVSRoaches](https://github.com/SoyGema/Startcraft/blob/master/Images/2C01EB1027814BB7FF16A15272E1B2DEF9FDEEC3.jpg)](https://www.youtube.com/watch?v=XvYWLRBf-5U "Scripted Agent MarinesVS Roaches" )

*   No map random exploration by agent
*   Increased number of victories by agent 
*   However, there seems to be a balance in between . 
*   In the middle of the game you can see player 1 is currently winning and the agent starts losing as it imbalance by rules games. 
*   Everytime the game is executed it shows an error at aproximately min 15 
*  Error has been reported to blizzard team 


## 2. Getting into Starcraft 2 Map Editor 

#### 2.1 Changing units and reward shaping 

Starcraft 2 Map Editor is an extensive piece of software that might be studied independly.
There are currently great tutorials at battlenet in wich you can find detailed information about map creations . You might want to 
By now, the most significant concepts that minigame creation need are 

*Terrain. Set the physical environment for your game including playable space and start units
*Triggers . Basic set of instructions and visual programming interface in wich you can set important variables such as : events, conditions and actions 

Inside your Starcraft II folder you should find an executable file for StarCraft II Editor . When you open MarinesVSRoach.SC2Maps you should find something like this 
##### Terrain
In this screen you might find a terrain configuration. Playable space and Right / Left areas are settled for different players. In the upper band you might find common open/save  copy/paste settings options and unit/terrain edition.

![alt tag](https://github.com/SoyGema/Startcraft/blob/master/Images/Captura%20de%20pantalla%202017-09-08%20a%20las%2017.05.07.png)
The playable regions will be related to players in the triggers 
The first thing that you might find curious is that there are no units settled down in the terrain . 
They are settled in the init visual script 

##### Triggers
![alt tag](https://github.com/SoyGema/Startcraft_pysc2_minigames/blob/master/Images/trigger.png)
In the top bar you might see an ico 
Triggers are divided into List / content full interfaces.
The list shows the variables that you set in your minigame ( in this case a timer, a marine and a roach variable) in wich conditions are created in diferent scripts 
![alt tag](https://github.com/SoyGema/Startcraft/blob/master/Images/Captura%20de%20pantalla%202017-09-08%20a%20las%2017.48.55.png)

On the left side you can find the trigger list you might need for your map creation. In that list we define some as variables and another ones as visual script that will have a complete function.
Common to all minimaps we have Init trigger, in wich we will setup initial conditions for the minimap .
Top right to trigger list we will find trigger content , in wich we will expand options for init trigger to function. We will find 4 options common to all minimaps 


#### Action Triggers : defining functioning

##### Init Triggers : defining inizialization
###### Map Triggers
We divide action triggers into different cattegories : map setup, scenario, Initial score and objetive. In the action triggers map setup we find at first Playable Space setup wich we must link to the terrain edition we made earlier , and set camera options in order to make the playable space camera setup accordingly 
Note that there you might find trigger conditions if/then/else: visual programming scripting for settle down map conditions. In this case we are stablishing the condition that if player 1 is distint from computer player, then Locks the camera in place for a player, causing the player to be unable to move the camera in any way -settle by cameraLockInputTrigger-.In other case reveals the specified region for the specified duration of time and increases velocity game. 

![alt tag](https://github.com/SoyGema/Startcraft_pysc2_minigames/blob/master/Images/Captura%20de%20pantalla%202017-09-17%20a%20las%2013.09.44.png) MapSetup trigger visual scrip inizialization

###### Changing unit inizialization in Init visual script 
In the init script you might find  two ways to create the units :

![alt tag](https://github.com/SoyGema/Startcraft_pysc2_minigames/blob/master/Images/change_units.png)

 ---- A for loop going from 1 to 9 creating Marine unit whith an offset , adding it to a variable created ( Marines ). Renaming this variable into the name of your unit will help you to have 
 If you double click , in the "Type" section you can select any other unit . In this case I selected sentry 
![alt tag](https://github.com/SoyGema/Startcraft_pysc2_minigames/blob/master/Images/change%20Marines.png)


----- An inizialization of units added to the group as a variable defined . In this case, several Roaches.
I will change it for Zerlings 
![alt tag]()

Now, the script should look like this 
This means that now the initial setup must be Sentry VS Chalenging (Zerlings) 
![alt tag](https://github.com/SoyGema/Startcraft_pysc2_minigames/blob/master/Images/new_init.png)

###### Reward Shaping in Score Updates and Victory script 
This script basically 


# Index

## 1 - Terran
1.1 - [Terran](Terran/Terran_mini_ganes.md)
1.2 - [Zerg](Zerg/Zerg_mini_games.md)
1.3 - [Protoss](Protoss/Protoss_mini_games.md)


Startcraft dataset and AI research 
## Another  Useful resources about Startcraft 
DeepMind paper

DataSet exploration
https://arxiv.org/pdf/1708.02139.pdf
Pysc2 deepmind reserach paper

Link to Pysc2 repository 
https://github.com/deepmind/pysc2
