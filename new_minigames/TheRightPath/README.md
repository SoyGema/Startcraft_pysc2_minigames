#### Description
The mini-game is a problem of finding the optimal path in order to move a marine into a beacon, picking up minerals and avoiding mines
Each time a marine moves to the beacon the becon changes its position 


#### Initial State

*   1 Marine
*   1 Beacon
*   4 mines randomly distributed 
*   20 minerals shards to collect

#### Rewards

*   Mineral collected : +1
*   Beacon reached : +10

#### End Conditions

*   Time elapsed
*   Terran defeated

#### Time Limit

*   60 seconds

#### Additional Notes

*   Fog of war disabled 
*   No camera movement required (single-screen)
*   Note that this map is under development and should be re-sized for balance 
*   Please note this work is still under development. If you find any relevant comment or issue feel free to open an issue 


#### Intended machine Learning objetive 
Find the optimal path to the beacon while avoiding death
The behaviour that will separate good agents from bad ones : bad agents will go strictly to the beacon. Good agents will try to 
get minerals while getting there .


kudos : @flipper83
