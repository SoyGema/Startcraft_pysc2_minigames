# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# Special thanks to : jmathison
#                     thebunny 
#                     AleKahpwn

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy
import random

from pysc2.agents import base_agent
from pysc2.lib import actions
from pysc2.lib import features


FUNCTIONS = actions.FUNCTIONS
_PLAYER_RELATIVE = features.SCREEN_FEATURES.player_relative.index
_PLAYER_FRIENDLY = 1
_PLAYER_NEUTRAL = 3  # beacon/minerals
_PLAYER_HOSTILE = 4
_NO_OP = FUNCTIONS.no_op.id
_MOVE_SCREEN = FUNCTIONS.Move_screen.id
_ATTACK_SCREEN = FUNCTIONS.Attack_screen.id
_SELECT_ARMY = FUNCTIONS.select_army.id
_NOT_QUEUED = [0]
_SELECT_ALL = [0]
_HAL_ADEPT = FUNCTIONS.Hallucination_Adept_quick.id
_HAL_ARCHON = FUNCTIONS.Hallucination_Archon_quick.id
_HAL_COL = FUNCTIONS.Hallucination_Colossus_quick.id
_HAL_DISRUP = FUNCTIONS.Hallucination_Disruptor_quick.id
_HAL_HIGTEM = FUNCTIONS.Hallucination_HighTemplar_quick.id
_HAL_IMN = FUNCTIONS.Hallucination_Immortal_quick.id
_HAL_PHOENIX = FUNCTIONS.Hallucination_Phoenix_quick.id
_HAL_STALKER = FUNCTIONS.Hallucination_Stalker_quick.id
_HAL_VOIDRAID = FUNCTIONS.Hallucination_VoidRay_quick.id
_HAL_ZEALOT = FUNCTIONS.Hallucination_Zealot_quick.id
_FORCE_FIELD = FUNCTIONS.Effect_ForceField_screen.id
_GUARD_FIELD = FUNCTIONS.Effect_GuardianShield_quick.id

class SentryForceField(base_agent.BaseAgent):
  """An agent specifically for solving the ForceField map."""

  def step(self, obs):
    super(SentryForceField, self).step(obs)
    if _FORCE_FIELD in obs.observation["available_actions"]:
      player_relative = obs.observation.feature_screen.player_relative
      hydralisk_y, hydralisk_x = (player_relative == _PLAYER_HOSTILE).nonzero()
      if not hydralisk_y.any():
        return FUNCTIONS.no_op()
      index = numpy.argmax(hydralisk_y)
      target = [hydralisk_x[index], hydralisk_y[index]]
      return FUNCTIONS.Effect_ForceField_screen("now", target)
    elif _SELECT_ARMY in obs.observation["available_actions"]:
      return FUNCTIONS.select_army("select")
    else:
      return FUNCTIONS.no_op()

Hallucinations_list = [_HAL_ADEPT, _HAL_ARCHON, _HAL_DISRUP, _HAL_HIGTEM, _HAL_IMN, _HAL_PHOENIX, _HAL_STALKER, _HAL_VOIDRAID, _HAL_ZEALOT]

  
  
class HallucinationArchon(base_agent.BaseAgent):
  """An agent specifically for solving the HallucinIce map with Archon Unit."""

  def step(self, obs):
    super(HallucinationArchon, self).step(obs)
    if _HAL_ARCHON in obs.observation["available_actions"]:
      player_relative = obs.observation["feature_screen"][_PLAYER_RELATIVE]
      hellion_y, hellion_x = (player_relative == _PLAYER_HOSTILE).nonzero()
      if not hellion_y.any():
        return actions.FunctionCall(_NO_OP, [])
      index = numpy.argmax(hellion_y)
      target = [hellion_x[index], hellion_y[index]]
      return actions.FunctionCall(_HAL_ARCHON, [_NOT_QUEUED])
    elif _SELECT_ARMY in obs.observation["available_actions"]:
      return actions.FunctionCall(_SELECT_ARMY, [_SELECT_ALL])
    else:
      return actions.FunctionCall(_NO_OP, [])

    
Hallucinations = [_HAL_ADEPT, _HAL_ARCHON, _HAL_DISRUP, _HAL_HIGTEM, _HAL_IMN, _HAL_PHOENIX, _HAL_STALKER, _HAL_VOIDRAID, _HAL_ZEALOT]

class Hallucination(base_agent.BaseAgent):
  """An agent specifically for solving the HallucinIce map with Random Hallucination."""

  def step(self, obs):
    test = random.randrange(0, len(Hallucinations_list) - 1)
    super(Hallucination, self).step(obs)

    score_general = obs.observation["score_cumulative"][0]
    value_units = obs.observation["score_cumulative"][3]
    kill_value_units = obs.observation["score_cumulative"][5]

    print("score general is ", score_general)
    print("value units is ", value_units)
    print("kill value units is", kill_value_units)

    if Hallucinations_list[test] in obs.observation["available_actions"]:
      player_relative = obs.observation["feature_screen"][_PLAYER_RELATIVE]
      hellion_y, hellion_x = (player_relative == _PLAYER_HOSTILE).nonzero()
      if not hellion_y.any():
        return actions.FunctionCall(_NO_OP, [])
      index = numpy.argmax(hellion_y)
      target = [hellion_x[index], hellion_y[index]]
      print(random.randrange(0, len(Hallucinations_list)))

      return actions.FunctionCall(Hallucinations_list[test], [_NOT_QUEUED])
    elif _SELECT_ARMY in obs.observation["available_actions"]:
      return FUNCTIONS.select_army("select")
    else:
      return FUNCTIONS.no_op()

   
 class StalkerControl(base_agent.BaseAgent):
  """An agent specifically for solving the DefeatZealotsMap map without Blink but with micro  """  

    base_top_left = None  
  
    def transformLocation(self, x, x_distance, y, y_distance):
        if not self.base_top_left:
            return [x - x_distance, y - y_distance]=
        return [x + x_distance, y + y_distance]
      
      
  def step(self, obs):
    super(StalkerControl, self).step(obs)
    if _______ in obs.observation["available_actions"]:
      player_relative = obs.observation["feature_screen"][_PLAYER_RELATIVE]
      zealot_y, zealot_x = (player_relative == _PLAYER_HOSTILE).nonzero()
      if not zealot_y.any():
        return actions.FunctionCall(_NO_OP, [])
      index = numpy.argmax(zealot_y)
      target = [zealot_x[index], zealot_y[index]]
      return actions.FunctionCall(_________, [_NOT_QUEUED])
    elif _SELECT_ARMY in obs.observation["available_actions"]:
      return actions.FunctionCall(_SELECT_ARMY, [_SELECT_ALL])
    else:
      return actions.FunctionCall(_NO_OP, [])
