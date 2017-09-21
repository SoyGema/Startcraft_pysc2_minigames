## Sentry Defense mini-game Map

![alt tag](https://github.com/SoyGema/Startcraft_pysc2_minigames/blob/master/Images/Captura%20de%20pantalla%202017-09-18%20a%20las%2020.14.14.png)

#### Description
The mini-game is a melee in between Terran marauders and marines and Protoss Stalker and Sentry units on opposite sides.
The goal for agent research is to maximize the utility -explotation- of sentry unit defense, hallucination and sield unit functions
Both armys are disposed in two playable spaces with Arrowhead formation, presented as an end of movement phase.
Sentry unit is disposed as Leader with special weapon position.



#### Initial State

*   7 Marines at left playable size
*   4 Marauders at left playable size disposed as leader in arrowhead formation
*   5 Stalkers at right playable size 
*   4 Sentry at right playable size disposed as leader in arrowhead formation 

#### Rewards

*   Protoss defeated : -1
*   Terran defeated : +10

#### End Conditions

*   Time elapsed
*   Terran defeated

#### Time Limit

*   120 seconds

#### Additional Notes

*   Fog of war disabled 
*   No camera movement required (single-screen)
*   Note that this map is under development and should be re-sized for balance 
*   Please note this work is still under development. If you find any relevant comment or issue feel free to open an issue 

#### Tutorial
Find a tutorial about another minigame at https://soygema.github.io/Startcraft_pysc2_minigames/

