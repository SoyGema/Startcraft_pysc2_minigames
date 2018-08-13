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

-- q_learning_agent.py --- >  learning agent - Tested - 

-- DQN_Agent.py --- > learning agent - Tested - 

-- DQN_Agent_LSTM.py --- > learning agent - Tested - Architecture bellow

After executing file, type in console :

```
$ tensorboard --logdir path/Graph
```
![alt tag](https://github.com/SoyGema/Startcraft_pysc2_minigames/blob/master/Images/Captura%20de%20pantalla%202018-08-13%20a%20las%2015.43.15.png)


### Debugging and testing 


#### Print available actions 

Will print the id of the available actions in a list 

        action_no = actions.FunctionCall(_NO_OP, [])
        obs_no = super(Environment, self).step([action_no])
        actions_available = obs_no[0].observation.available_actions
        print(actions_available) 
