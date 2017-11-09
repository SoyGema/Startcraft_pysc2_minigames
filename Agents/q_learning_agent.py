# Q-learning agent for HallucinIce. 
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

_NO_OP = actions.FUNCTIONS.no_op.id
_MOVE_SCREEN = actions.FUNCTIONS.Move_screen.id
_ATTACK_SCREEN = actions.FUNCTIONS.Attack_screen.id
_SELECT_ARMY = actions.FUNCTIONS.select_army.id
_NOT_QUEUED = [0]
_SELECT_ALL = [0]

# Define the actions 
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
  ACTION_HAL_ZEALOT 
]

KILL_UNIT_REWARD = 0.5


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
      
  
class SmartAgent(base_agent.BaseAgent):
  def __init__(self):
    self.qlearn = QLearningTable(actions=list(range(len(smart_actions))))
    
    self.previous_killed_unit_score = 0
    self.previous_action = None
    self.previous_state = None 
    
    #Compare step from scripted agent with learning agent 
  def step(self, obs):
    #-----------------#
    #---#
    #---#
    
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

