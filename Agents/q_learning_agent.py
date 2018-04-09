# Q-learning agent for HallucinIce. 
# The goal for the agent is to discover wich combination of hallucination will be better to defeat 
# Kudos to Steven Brown and to MorvanZhou 

import random
import math 

import numpy as np
import pandas as pd 

from pysc2.agents import base_agent
from pysc2.lib import actions
from pysc2.lib import features 

#Features
_PLAYER_RELATIVE = features.SCREEN_FEATURES.player_relative.index
_PLAYER_FRIENDLY = 1
_PLAYER_HOSTILE = 4 
_UNIT_TYPE = features.SCREEN_FEATURES.unit_type.index
_PLAYER_ID = features.SCREEN_FEATURES.player_id.index
#Functions
_NO_OP = actions.FUNCTIONS.no_op.id
_SELECT_POINT = actions.FUNCTIONS.select_point.id 
_MOVE_SCREEN = actions.FUNCTIONS.Move_screen.id
_ATTACK_SCREEN = actions.FUNCTIONS.Attack_screen.id
_SELECT_ARMY = actions.FUNCTIONS.select_army.id #Attack_minimap.id
#Parameters
_NOT_QUEUED = [0]
_SELECT_ALL = [0]

#Unit IDs
PROTOSS_SENTRY = 77
TERRAN_HELLION = 53

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

#Define the call to the API of the Hallucination function 
_HAL_ADEPT = actions.FUNCTIONS.Hallucination_Adept_quick.id
_HAL_ARCHON = actions.FUNCTIONS.Hallucination_Archon_quick.id
_HAL_COL = actions.FUNCTIONS.Hallucination_Colossus_quick.id
_HAL_DISRUP = actions.FUNCTIONS.Hallucination_Disruptor_quick.id
_HAL_HIGTEM = actions.FUNCTIONS.Hallucination_HighTemplar_quick.id
_HAL_IMN = actions.FUNCTIONS.Hallucination_Immortal_quick.id
_HAL_PHOENIX = actions.FUNCTIONS.Hallucination_Phoenix_quick.id
_HAL_STALKER = actions.FUNCTIONS.Hallucination_Stalker_quick.id
_HAL_VOIDRAID = actions.FUNCTIONS.Hallucination_VoidRay_quick.id
_HAL_ZEALOT = actions.FUNCTIONS.Hallucination_Zealot_quick.id
_FORCE_FIELD = actions.FUNCTIONS.Effect_ForceField_screen.id
_GUARD_FIELD = actions.FUNCTIONS.Effect_GuardianShield_quick.id

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
  ACTION_ATTACK,
]

KILL_UNIT_REWARD = 0.5


class QLearningTable:
  def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9):
      self.actions = actions # a list? 
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
        
        action = state_action.idxmax()
      else :
      # choose random action 
        action = np.random.choice(self.actions)
        
      return action
  
  #Q-learning implementation
  
  def learn(self, s, a, r, s_):
      self.check_state_exist(s_)
      self.check_state_exist(s)
      
      #Make q-table and select max value 
      
      q_predict = self.q_table.ix[s, a]
      q_target = r + self.gamma * self.q_table.ix[s_, :].max()
      
      # update 
      
      self.q_table.ix[s, a] += self.lr * (q_table - q_predict)
      
  def check_state_exist(self, state):
      if state not in self.q_table.index:
        self.q_table = self.q_table.append(pd.Series([0] * len(self.actions), index=self.q_table.columns, name=state))
      
  
class SmartAgent(base_agent.BaseAgent):
  def __init__(self):
    super(SmartAgent, self).__init__() #For fix trouble with undefined properties 
    self.qlearn = QLearningTable(actions=list(range(len(smart_actions))))
    
    self.previous_killed_unit_score = 0
    self.previous_action = None
    self.previous_state = None 
 

  #Helper method so that we can work with locations relative to the base
  def transformLocation(self, x, x_distance, y, y_distance):
      if not self.base_top_left:
          return [x - x_distance, y - y_distance]
      return [x + x_distance, y + y_distance]

    #Compare step from scripted agent with learning agent 
  def step(self, obs):
      super(SmartAgent, self).step(obs)
    #---#
      player_y, player_x = (obs.observation['minimap'][_PLAYER_RELATIVE] == _PLAYER_FRIENDLY).nonzero()
      self.base_top_left = 1 if player_y.any() and player_y.mean() <= 31 else 0
    
    ##unit_type = obs.observation['screen'][_UNIT_TYPE] is this here or inside fork ? 
      current_state = [
          n_sentry_count,
          hallucinations_count,
          n_enemies_count,
          army_supply,  # this comma exists?
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
      
      elif smart_action == ACTION_SELECT_SENTRY:
        unit_type = obs.observation['screen'][_UNIT_TYPE]
        unit_y, unit_x = (unit_type == _SENTRY).nonzero()
      
        if unit_y.any():
            i = random.randint(o, len(unit_y) -1)
            target = [unit_x[i], unit_y[i]]
        
            return actions.FunctionCall(_SELECT_POINT, [_NOT_QUEUED, target])

    
      elif smart_action == ACTION_HAL_ARCHON:
        if _HAL_ARCHON in obs.observation["available_actions"]:
            return actions.FunctionCall(_HAL_ARCHON, [_NOT_QUEUED])
    
      elif smart_action == ACTION_HAL_ADEPT:
        if _HAL_ADEPT in obs.observation["available_actions"]:
            return actions.FunctionCall(_HAL_ADEPT, [_NOT_QUEUED])
    
      elif smart_action == ACTION_HAL_COL:
        if _HAL_COL in obs.observation["available_actions"]:
            return actions.FunctionCall(_HAL_ADEPT, [_NOT_QUEUED])

      elif smart_action == ACTION_HAL_DISRUP:
        if _HAL_DISRUP in obs.observation["available_actions"]:
            return actions.FunctionCall(_HAL_ADEPT, [_NOT_QUEUED])
    
      elif smart_action == ACTION_HIGTEM:
        if _HAL_HIGTEM in obs.observation["available_actions"]:
            return actions.FunctionCall(_HAL_ADEPT, [_NOT_QUEUED])
    
      elif smart_action == ACTION_PHOENIX:
        if _HAL_PHOENIX in obs.observation["available_actions"]:
            return actions.FunctionCall(_HAL_ADEPT, [_NOT_QUEUED])
    
    
      elif smart_action == ACTION_STALKER:
        if _HAL_STALKER in obs.observation["available_actions"]:
            return actions.FunctionCall(_HAL_ADEPT, [_NOT_QUEUED])

      elif smart_action == ACTION_ATTACK:
        if _ATTACK_MINIMAP in obs.obsservation["available_actions"]:
            if self.base_top_left:
                return actions.FunctionCall(_ATTACK_MINIMAP, [_NOT_QUEUED], [77, 53])

            return actions.FunctionCall(_ATTACK_MINIMAP, [_NOT_QUEUED], [77, 53])

      return actions.FunctionCall(_NO_OP, [])
