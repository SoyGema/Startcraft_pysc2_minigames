
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

episode_reward = 0

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
    return batch[0]

## Agent architecture using keras rl 


### Model
# Agents representation of the environment. ( How the agent thinks the environment works) 

#### 1. 256 , 127, 256 are the channels- depth of the first layer, one can be colour, edges)
#### 2. Kernel size is the size of the matrix it will be use to make the convolution ( impair size is better)
#### 3. strides are the translation that kernel size will be making 

def create_model(input, actions):
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


### Policy 
# Agent´s behaviour function. How the agent pick actions

policy = LinearAnnealedPolicy(EpsGreedyQPolicy(), attr="eps", value_max=1, value_min=0.7, value_test=.0, nb_steps=1e6)

### Agent
#
            
dqn = DQNAgent(model=model, nb_actions=action, memory=memory, nb_steps_warmup=50, target_model_update=1e-2, policy=policy)
