
#### Description
The mini-game is a challenge for defending against waves of zergs 
Choose your favorite race and defend against incremental zerg attacks

#### Initial State
Choose the race you will be by typing in the chat message bar : terran (for Terran) , zerg (for zerg) or protoss (for protoss)

if choose playing with Terran, your initial conditions will be 
*   1 Command center 
*   10  SCV
*   50 minerals  

if choose playing with zerg, your initial conditions will be 
*   1 Hive 
*   10 drone
*   50 minerals

if choose playing with zerg, your initial conditions will be 
*   1 Nexus
*   10 Probe
*   50 minerals 

#### Wave description 
*   1st wave : 6 zerlings
*   2nd wave : 4 changeling with wings
*   3rd wave : 4 roaches
*   4th wave : 4 roaches (upgraded) + 4 changelling 
*   5th wave : 6 changelling (upgraded) 
*   6th wave : 4 roaches (upgraded) + 4 changelling (upgraded)
*   7th wave : 6 hydralisks
*   8th wave : 4 mutas
*   9th wave : 4 mutas + 4 roaches
*   10th wave : 1 Ultralisk

#### Rewards

*   units dead in zerg group : +10

#### End Conditions

*   Time elapsed
*   Zerg defeated

#### Time in between each wave 

*   30, 45 and/or 60 seconds , depending on the wave 

#### Additional Notes

*   Note that this map is under development and should be re-sized for balance 
*   Please note this work is still under development. If you find any relevant comment or issue feel free to open an issue 


#### Intended machine Learning objetive 
Find the optimal unit defense positions nad units to defend against attack zerg waves. 
The behaviour that will separate good agents from bad ones : bad agents will produce a random army. Good agents will try to 
get a balance army including air .
