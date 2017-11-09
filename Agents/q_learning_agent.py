# Q-learning agent for HallucinIce. 
# The goal for the agent is to discover wich combination of hallucination will be better to defeat 
# Kudos to MorvanZhou , Steven Brow

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

_NO_OP = actions.FUNCTIONS.no_op.id
_MOVE_SCREEN = actions.FUNCTIONS.Move_screen.id
_ATTACK_SCREEN = actions.FUNCTIONS.Attack_screen.id
_SELECT_ARMY = actions.FUNCTIONS.select_army.id
_NOT_QUEUED = [0]
_SELECT_ALL = [0]


class QLearnigTable:
  def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9):
      self.actions = actions
      self.lr = learning_rate
      self.gamma = reward_decay
      self.epsilon = e_greedy
      self.q_table = pd.DataFrame(columns=self.actions)
      
  def choose_action(self, observation):
      self.check_state_exist(observation)
      
      if np.random.uniform() < self.epsilon:
      #choose the best action from q-table
        state_action = self.q_table.ix[observation, :]
        
      # some actions have the same value
        state_action = state_action.reindex(np.random.permutation(state_action.index))
        
        action = state_action.argmax()
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
        self.q_table = self.q_table.append(pd.Series([0] * len(self.actions), index=self.q_table.columns, name=state))
      
  
# Define the actions 
_HAL_ADEPT = 'adept'
_HAL_ARCHON = 'archon'
_HAL_COL = 'colosus'
_HAL_DISRUP = 'disruptor'
_HAL_HIGTEM = 'higtem'
_HAL_IMN = 'imortal'
_HAL_PHOENIX = 'phoenix'
_HAL_STALKER = 'stalker'
_HAL_VOIDRAID = 'voidraid'
_HAL_ZEALOT = 'zealot'

#Smart actions = [
  _HAL_ADEPT,
  _HAL_ARCHON,
  _HAL_COL,
  _HAL_DISRUP,
  _HAL_HIGTEM,
  _HAL_IMN,
  _HAL_PHOENIX,
  _HAL_STALKER,
  _HAL_VOIDRAID,
  _HAL_ZEALOT 
]



