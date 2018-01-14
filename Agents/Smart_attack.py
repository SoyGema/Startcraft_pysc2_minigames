 #Q-learning agent for HallucinIce with Smart Attack . 
# The goal for the agent is to discover wich combination of hallucination will be better to defeat 
# Kudos to MorvanZhou , Steven Brown

import random
import math 

import numpy as np
import pandas as pd 

from pysc2.agents import base_agent
from pysc2.lib import actions
from pysc2.lib import features 

_PLAYER_RELATIVE = features.SCREEN_FEATURES.player_relative.index
_PLAYER_FRIENDLY = 1
_PLAYER_HOSTILE = 4 
_UNIT_TYPE = features.SCREEN_FEATURES.unit_type.index
_PLAYER_ID = features.SCREEN_FEATURES.player_id.index

_NO_OP = actions.FUNCTIONS.no_op.id
_MOVE_SCREEN = actions.FUNCTIONS.Move_screen.id
_ATTACK_SCREEN = actions.FUNCTIONS.Attack_screen.id
_SELECT_ARMY = actions.FUNCTIONS.select_army.id
_NOT_QUEUED = [0]
_SELECT_ALL = [0]

# Define the actions 
ACTION_DO_NOTHING = 'donothing'
ACTION_SELECT_SENTRY = 'selectsentry'
ACTION_HAL_ADEPT = 'adept'
ACTION_HAL_ARCHON = 'archon'
ACTION_HAL_COL = 'colosus'
ACTION_HAL_DISRUP = 'disruptor'
ACTION_HAL_HIGTEM = 'higtem'
ACTION_HAL_IMN = 'imortal'
ACTION_HAL_PHOENIX = 'phoenix'
ACTION_HAL_STALKER = 'stalker'
ACTION_HAL_VOIDRAID = 'voidraid'
ACTION_HAL_ZEALOT = 'zealot'
ACTION_ATTACK = 'attack'

Smart_actions = [
  ACTION_NO_OP,
  ACTION_HAL_ADEPT,
  ACTION_HAL_ARCHON,
  ACTION_HAL_COL,
  ACTION_HAL_DISRUP,
  ACTION_HAL_HIGTEM,
  ACTION_HAL_IMN,
  ACTION_HAL_PHOENIX,
  ACTION_HAL_STALKER,
  ACTION_HAL_VOIDRAID,
  ACTION_HAL_ZEALOT,
]

# Alter the attack action
#The smart_actions variable contains an acton to attack any x,y map combination. 

for mm_x in range(0, 64):
 for mm_y in range(0, 64):
     if (mm_x + 1) % 16 == 0 and (mm_y + 1) % 16 == 0:
         smart_actions.append(ACTION_ATTAC + '_' + str(mm_x - 8) + '_' + str(mm_y -8))
         
KILL_UNIT_REWARD = 0.5


class QLearnigTable:
  def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9):
      self.actions = actions
      self.lr = learning_rate
      self.gamma = reward_decay
      self.epsilon = e_greedy
      self.q_table = pd.DataFrame(columns=self.actions, dtype=np.float64)
      
  def choose_action(self, observation):
      self.check_state_exist(observation)
      
      if np.random.uniform() < self.epsilon:
      #choose the best action from q-table
        state_action = self.q_table.ix[observation, :]
        
      # some actions have the same value
        state_action = state_action.reindex(np.random.permutation(state_action.index))
        
        action = state_action.idmax()
      else :
      # choose random action 
        action = np.random.choice(self.actions)
        
      return action
  
  #Q-learning implementation
  
  def learn(self, s, a, r, s_):
      self.check_state_exist(s_)
      self.check_state_exist(s)
      
      #Make q-table and select max value 
      
      q_pedict = self.q_table.ix[s, a]
      q_target = r + self.gamma * self.q_table.ix[s_, :].max
      
      # update       
      self.q_table.ix[s, a] += self.lr * (q_table - q_predict)
      
  def check_state_exist(self, state):
      if state not in self.q_table.index:
        # append new state to q-table
        self.q_table = self.q_table.append(pd.Series([0] * len(self.actions), index=self.q_table.columns, name=state))
      
  
class AttackAgent(base_agent.BaseAgent):
  def __init__(self):
    super(AttackAgent, self).__init__() #For fix trouble with undefined properties 
    self.qlearn = QLearningTable(actions=list(range(len(smart_actions))))
    
    self.previous_killed_unit_score = 0
    self.previous_action = None
    self.previous_state = None 
 
    # Define method converts absolute x and y values based on the location of your base.
    # These methods are use for SVC building 
   
  def transformDistance(self, x, x_distance, y, y_distance):
      if not self.bas_top_left:
          return [x - x_distance, y + y_distance]
     
      return [x + x_distance, y + y_distance]
     
  def transformLocation(self, x, y):
      if not self.base_top_left:
          return [64 -x, 64 -y]
     
      return [x,y]
 
    #Compare step from scripted agent with learning agent 
  def step(self, obs):
    super(AttackAgent, self).step(obs)
    #---#
    player_y, player_x = (obs.observation['minimap'][_PLAYER_RELATIVE] == _PLAYER_FRIENDLY).nonzero()
    self.base_top_left = 1 if player_y.any() and player_y.mean() <= 31 else 0
    
    if smart_action == ACTION_DO_NOTHING:
      return actions.FunctionCall(_NO_OP), [])
      
    elif smart_action == ACTION_SELECT_SENTRY:
      unit_type = obs.observation['screen'][_UNIT_TYPE]
      unit_y, unit_x = (unit_type == _SENTRY).nonzero()
      
      if unit_y.any():
        i = random.randint(o, len(unit_y) -1)
        target = [unit_x[i], unit_y[i]]
        
        return actions.FunctionCall(_SELECT_POINT, [_SCREEN, target])
        
        
        current_state = [
            n_sentry_count,
            hallucinations_count,
            n_enemies_count,
            army_supply,
        ]   
        
        
    if self.previous_action is not None:
      reward = 0
      
      if killed_unit_score > self.previous_killed_score:
        reward += KILL_UNIT_REWARD
        
      self.qlearn.learn(str(self.previous_state), self.previous_action, reward, str(current_state))
    
    rl_action = self.qlearn.choose_action(str(current_state))
    smart_action = smart_actions[rl_action]
    
    self.previous_killed_unit_score = killed_unit_score
    self.previous_state = current_state
    self.previous_action = rl_action
    
    if smart_action == ACTION_DO_NOTHING:
      return actions.FunctionCall(_NO_OP, [])
    
    elif smart_action == ACTION_HAL_ARCHON:
      if _HAL_ARCHON in obs.observation["available_actions"]:
        player_relative = obs.observation["screen"][_PLAYER_RELATIVE]
        hellion_y, hellion_x = (player_relative = _PLAYER_HOSTILE).nonzero()
      return actions.FunctionCall(_HAL_ARCHON, [_NOT_QUEUED])
     
    elif smart_action == ACTION_ATTACK:
      if _ATTACK_MINIMAP in obs.observation["available_actions"]:
          return actions.FunctionCall(_ATTACK_MINIMAP, [_NOT_QUEUED, self.transformLocation(int(x), int(y))])
