# Sentry Agent mini-game Map exploration

This part of the repository aims to post several agents regarding functions of sentry unit. 
SentryDefense.py --contains all the actions for sentrydefense unit
scripted_agent.py --contains tests for Forcefield Starcraft 2 map 

### Sentry unit scripted bot running

--Clone the repo 

--Put ForceField.sc2 map into your minigames map folder 

--Go to pysc2/maps/mini_games.py and add ForceField map to the array map

--In the /pysc2/agents/ folder type 

```
$ python3 -m pysc2.bin.agent --agent scripted_agent.SentryForceField --map ForceField
```
### About the agents 

-- scripted_gent.py --- > scripted -Tested-

-- q_learning_agent.py --- >  learning agent - not Tested - under development 

-- DQN_Agent.py --- > learning agent - not Tested -under development 
