# Kudos to MorvanZhou , Steven Brow

import random
import math 

import numpy as np
import pandas as pd 

from pysc2.agents import base_agent
from pysc2.lib import actions
from pysc2.lib import features 

_NO_OP = actions.FUNCTIONS.no_op.id
_MOVE_SCREEN = actions.FUNCTIONS.Move_screen.id
_ATTACK_SCREEN = actions.FUNCTIONS.Attack_screen.id



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
      
     
