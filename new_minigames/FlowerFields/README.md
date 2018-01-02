## FlowerFields

![alt tag](https://github.com/SoyGema/Startcraft_pysc2_minigames/blob/master/Images/Captura%20de%20pantalla%202018-01-02%20a%20las%2014.51.09.png)


#### Description

Defeat protoss photon cannon without losing any marauder.
The goal of the minigame is to learn to regroup marauders and to attack in a coordinated way without losing any unit 

#### Initial State

*   4 photon cannon at Central playable size
*   2 marauders at right playable size
*   2 marauders at left playable size

 #### Rewards

Protoss defeated : +10
Terran defeated : -5

 #### End Conditions

Time elapsed
Protoss defeated
Time Limit

60 seconds
 #### Additional Notes
Terrain condition designed for photon defense game development 
Fog of war disabled
No camera movement required (single-screen)
Note that this map is under development and should be re-sized for balance
Please note this work is still under development. If you find any relevant comment or issue feel free to open an issue



### FlowerFields random agent running

--Clone the repo 

--Put FlowerFields.sc2 map into your minigames map folder 

--Go to pysc2/maps/mini_games.py and add FlowerFields map to the array map

--In the /pysc2/agents/ folder type 

```
$ python3 python3 -m pysc2.bin.agent  --map FlowerFields
```
