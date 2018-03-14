
import numpy as np
import sys

from keras.models import Sequential 
from keras.layers import Dense, Flatten, Convolution2D
from keras.optimizers import Adam, Adamax, Nadam
from keras.backend import set_image_dim_ordering

from pysc2.env import sc2_env, environment
from pysc2.lib import actions
from pysc2.lib import features

from rl.memory import SequentialMemory
from rl.policy import LinearAnnealedPolicy, EpsGreedyQPolicy
from rl.core import Processor
from rl.agents.dqn import DQNAgent , SARSAAgent


## Actions from pySC2 API  ( Move, attack, select , hallucination actions ) 

_PLAYER_RELATIVE = features.SCREEN_FEATURES.player_relative.index
_PLAYER_FRIENDLY = 1
_PLAYER_NEUTRAL = 3  # beacon/minerals
_PLAYER_HOSTILE = 4
_NO_OP = actions.FUNCTIONS.no_op.id
_MOVE_SCREEN = actions.FUNCTIONS.Move_screen.id
_ATTACK_SCREEN = actions.FUNCTIONS.Attack_screen.id
_SELECT_ARMY = actions.FUNCTIONS.select_army.id
_NOT_QUEUED = [0]
_SELECT_ALL = [0]
_HAL_ADEPT = actions.FUNCTIONS.Hallucination_Adept_quick.id
_HAL_ARCHON = actions.FUNCTIONS.Hallucination_Archon_quick.id

## Load and save weights for training 

LOAD_MODEL = True 
SAVE_MODEL = True

## global variable 

episode_reward = 0

## Processor 
# A processor acts as a relationship between an Agent and the Env . 
# useful if the agent has different requirements with respect to the form of the observations, actions, and rewards of environment
# How many frames will be an obs ?

class SC2Proc(Processor):
  def process_observation(self, observation):
    """Process the observation as obtained from the environment for use an agent and returns it""" 
    obs = observation[0].observation["screen"][_PLAYER_RELATIVE] #Read the features from the screen . This will change with pix2pix
    return obs
  
  def process_state_batch(self, batch):
    """Processes an entire batch of states and returns it"""
    return batch[0]
  
  def process_reward(self, reward):
    """Processes the reward as obtained from the environment for use in an agent and returns it """
    reward = 0
    return reward 

  
##  Define the environment

class Environment(sc2_env.SC2Env):
  """Starcraft II enviromnet. Implementation details in lib/features.py"""
  def step(self, action):
    """Apply actions, step the world forward, and return observations"""
    global episode_reward #global variable defined previously 
    
    action = actions_to_choose(action) #Actions of Hallucination and movement  Make a function that selects among hallucination functions
    obs = super(Environment, self).step([actions.FunctionCall(_MOVE_SCREEN, [_NOT_QUEUED, action])]) ## change the action for Hallucination?
    # The method calls an observation that moves the screen 
    
    observation = obs
    r = obs[0].reward
    done = obs[0].step_type == environment.StepType.LAST #Episode_over
    episode_reward += r
    
    return observation, r, done, {} #Return observation, reward, and episode_over 
  
  def reset(self):
    # reset the environment 
    global episode_reward
    episode_reward = 0
    super(Environment, self).reset()
    
    return super(Environment, self).step([actions.FunctionCall(_SELECT_ARMY,[_SELECT_ALL])])

  
def actions_to_choose(action):
  hall = [ HAL_ADEPT, _HAL_ARCHON ]
  y = min(int(np.ceil(action / _SIZE)), _SIZE - 1)
  x = int(action % _SIZE)
  hallucinate = actions.FunctionCall(_HAL_ARCHON, [_NOT_QUEUED])
  return y,x, hallucinate
  
## Agent architecture using keras rl 


### Model
# Agents representation of the environment. ( How the agent thinks the environment works) 

#### 1. 256 , 127, 256 are the channels- depth of the first layer, one can be colour, edges)
#### 2. Kernel size is the size of the matrix it will be use to make the convolution ( impair size is better)
#### 3. strides are the translation that kernel size will be making 

def neural_network_model(input, actions):
  model = Sequential()
  model.add(Convolutional2D(256, kernel_size=(5,5), input_shape=input))
  model.add(Activation('relu'))
  
  model.add(Convolution2D(127, kernel_size=(3,3))
  model.add(Activation('relu'))
  
  model.add(Convolution2D(32, kernel_size=(5,5))
  model.add(Activation('relu'))
  
  model.add(Flatten())
  model.add(Dense(actions))
  model.add(Activation('softmax')
  
  model.compile(loss="categorical_crossentropy",
  optimizer="adam",
  metrics=["accuracy"])

  return model            


            
def training_game():
  env = Environment(map_name="HallucinIce", visualize = True, game_steps_per_episode=150)
            
  input_shape = (_SIZE, _SIZE, 1)
  nb_actions = _SIZE * _SIZE  # Should this be an integer 
            
  model = neural_network_model(input_shape, action)  
# memory : how many subsequent observations should be provided to the network?            
  memory = SequentialMemory(limit=5e4, window_length=_WINDOW_LENGTH) 
  
  processor = SC2Proc()
            
### Policy 
# Agent´s behaviour function. How the agent pick actions
# LinearAnnealedPolicy is a wrapper that transforms the policy into a linear incremental linear solution . Then why im not see LAP with other than not greedy ?
# EpsGreedyQPolicy is a way of selecting random actions with uniform distributions from a set of actions . Select an action that can give max or min rewards
# BolztmanQPolicy . Assumption that it follows a Boltzman distribution. gives the probability that a system will be in a certain state as a function of that state´s energy??
                        
  policy = LinearAnnealedPolicy(EpsGreedyQPolicy(), attr="eps", value_max=1, value_min=0.7, value_test=.0, nb_steps=1e6)
  #policy = (BoltzmanQPolicy( tau=1., clip= (-500,500)) #clip defined in between -500 / 500 

                        
### Agent
# Double Q-learning ( combines Q-Learning with a deep Neural Network )
# Q Learning -- Bellman equation 
            
  dqn = DQNAgent(model=model, nb_actions=action, memory=memory,
                 nb_steps_warmup=50, target_model_update=1e-2, policy=policy,
                 batch_size = 150)
            
  dqn.compile(Adam(lr=.001), metrics=["mae"])
