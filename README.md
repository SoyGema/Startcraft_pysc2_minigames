
[![GitHub license](https://img.shields.io/github/license/SoyGema/Startcraft_pysc2_minigames.svg)](https://github.com/SoyGema/Startcraft_pysc2_minigames/blob/master/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/SoyGema/Startcraft_pysc2_minigames.svg)](https://github.com/SoyGema/Startcraft_pysc2_minigames/issues)
[![GitHub stars](https://img.shields.io/github/stars/SoyGema/Startcraft_pysc2_minigames.svg)](https://github.com/SoyGema/Startcraft_pysc2_minigames/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/SoyGema/Startcraft_pysc2_minigames.svg)](https://github.com/SoyGema/Startcraft_pysc2_minigames/network)
[![Twitter](https://img.shields.io/twitter/url/https/github.com/SoyGema/Startcraft_pysc2_minigames.svg?style=social)](https://twitter.com/intent/tweet?text=Pysc2_mini-games_by_@SoyGema:&url=https%3A%2F%2Fgithub.com%2FSoyGema%2FStartcraft_pysc2_minigames)

# Startcraft PySC2 mini-games and agents 
This repository aims to serve as a guide for open source contributing in minigame pysc2 library for Starcraft II
For minigame instalation for execution you should go to [the official repository](https://github.com/deepmind/pysc2) and install requirements

## Direct Links 
Please, if you want to reach directly mini-games click to the following [link](https://github.com/SoyGema/Startcraft_pysc2_minigames/blob/master/zip/mini-games.zip)

## Minigame task description
Minigames come as a controled environments that might be useful to exploit game features in SC2. General purpose learning system for Startcraft 2 can be a daunting task. So there is a logical option in splitting this tasks into minitask in orther to advance in research . Mini-games focus on different elements of Starcraft II Gameplay .

To investigate elements of the game in isolation, and to provide further fine-grained steps towards playing the full game, Deepmind has  built several mini-games. These are focused scenarios on small maps that have been constructed with the purpose of testing a subset of actions and/or game mechanics with a clear reward structure. Unlike the full game where the reward is just win/lose/tie, the reward structure for mini-games can reward particular behaviours (as defined in a corresponding .SC2Map file).

## Minigame introduction and Repo information
Before creating a minigame, I encourage you to run the alredy developed ones to see wich task are subdivided into each minigame as the reward function could be important due to the behaviour that leads to learning . The minigame title gives us a description of the goal 
You might find in this repo new maps created for investigate in explotation-exploration dilema and some programming about the functions of different units .

## SentryDefense , ForceField , HallucinIce  and FlowerFields Projects 

In this repo, besides information about current minigames, you will find my own minigames development . 
In projects section you can know more about the state of the art and in docs and new_minigames folder you can find the map.
In SentryDefense, a arrowhead TerranVSProtoss Melee is proposed .
In ForceField,an imbalanced situation between Sentry and Zerg units forces sentry to use forcefield, adding terrain disposition.

1.- [SentryDefense](https://github.com/SoyGema/Startcraft_pysc2_minigames/tree/master/new_minigames/SentryDefense): Protoss VS Terran Melee.

2.- [ForceField](https://github.com/SoyGema/Startcraft_pysc2_minigames/tree/master/new_minigames/SentryForceField): Learn about Sentry forcefield function. 

3.- [HallucinIce](https://github.com/SoyGema/Startcraft_pysc2_minigames/tree/master/new_minigames/SentryHallucination): Learn how to play with hallucination. 

4.- [FlowerFields](https://github.com/SoyGema/Startcraft_pysc2_minigames/tree/master/new_minigames/FlowerFields): Defeat protoss photon cannon . 

5.-[TheRightPath](https://github.com/SoyGema/Startcraft_pysc2_minigames/tree/master/new_minigames/TheRightPath): Move to beacon finding the optimal route collecting minerals and avoiding mines .

6.-[RedWaves](https://github.com/SoyGema/Startcraft_pysc2_minigames/tree/master/new_minigames/RedWaves): Choose your race and defend against waves of zerg attacks .

7.-[BlueMoon](https://github.com/SoyGema/Startcraft_pysc2_minigames/tree/master/new_minigames/BlueMoon): Choose unit development to defend against protoss development . (under construction) 

8.-[MicroPrism](https://github.com/SoyGema/Startcraft_pysc2_minigames/tree/master/new_minigames/MicroPrism): Learn how to use Warp Prism in a protoss versus protoss stalker melee 

## Agents
Regarding scripted agent, there is a python file with several developments. Scriptedagent.py is focused on HallucinIce map in which makes Archon Hallucination. Besides there is another class that put all hallucination actions on a list and the agent chooses randomly in between those actions .

Q-Learning and DQN agents are provided for HallucinIce minigame with the new  PySC2 release 

An A3C trained agent has been tested with several minigames, reaching some of them a local optima . 
Please, report problems in issues if you currently find problems .

## How to run mini-games in your environment 

1. Download or clone the repository, or download all minigames clicking here

2. Place the .SC2 files into /Applications/StarCraft II/Maps/mini_games/  -sometimes the Map folder might not exist. If so, please create it-

3. Go to pysc2\maps\mini_games.py and add to mini-games array the following mini-games names 

```python
mini_games = [  ## This mini-games names should alredy been in your list
    "BuildMarines",  # 900s
    "CollectMineralsAndGas",  # 420s
    "CollectMineralShards",  # 120s
    "DefeatRoaches",  # 120s
    "DefeatZerglingsAndBanelings",  # 120s
    "FindAndDefeatZerglings",  # 180s
    "MoveToBeacon",  # 120s   ##Now you add this few lines 
    "SentryDefense", # 120s
    "ForceField", # 30s
    "HallucinIce", # 30s
    "FlowerFields", # 60s
    "TheRightPath", # 300s
    "RedWaves", # 180s
    "BlueMoon", # 60s
    "MicroPrism", # 45s
]
```
4. In your console, you can type the mini-game map name 

```console
my-computer:~ me$ python -m pysc2.bin.agent --map FlowerFields 
```
      
      
#### Tutorial
Find an ongoing  tutorial about how to create your own mini-game [here](https://github.com/SoyGema/Startcraft_pysc2_minigames/tree/master/docs)

#### Other repository 
With features with map placement [here](https://github.com/ttinies/sc2gameMapRepo)



'Making a reward function isn’t that difficult. The difficulty comes when you try to design a reward function that encourages the behaviors you want while still being learnable.'
-Deep Reinforcement Learning Doesn´t work yet , Alex Irpan [post](https://www.alexirpan.com/2018/02/14/rl-hard.html)- 
