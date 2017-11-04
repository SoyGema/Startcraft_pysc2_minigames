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
"""Scripted agents."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy

from pysc2.agents import base_agent
from pysc2.lib import actions
from pysc2.lib import features

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




class SentryForceField(base_agent.BaseAgent):
  """An agent specifically for solving the ForceField map."""

  def step(self, obs):
    super(SentryForceField, self).step(obs)
    if _FORCE_FIELD in obs.observation["available_actions"]:
      player_relative = obs.observation["screen"][_PLAYER_RELATIVE]
      hydralisk_y, hydralisk_x = (player_relative == _PLAYER_HOSTILE).nonzero()
      if not hydralisk_y.any():
        return actions.FunctionCall(_NO_OP, [])
      index = numpy.argmax(hydralisk_y)
      target = [hydralisk_x[index], hydralisk_y[index]]
      return actions.FunctionCall(_FORCE_FIELD, [_NOT_QUEUED, target])
    elif _SELECT_ARMY in obs.observation["available_actions"]:
      return actions.FunctionCall(_SELECT_ARMY, [_SELECT_ALL])
    else:
      return actions.FunctionCall(_NO_OP, [])

Hallucinations = [_HAL_ADEPT, _HAL_ARCHON, _HAL_DISRUP, _HAL_HIGTEM, _HAL_IMN, _HAL_PHOENIX, _HAL_STALKER, _HAL_VOIDRAID, _HAL_ZEALOT]

class HallucinationArchon(base_agent.BaseAgent):
  """An agent specifically for solving the ForceField map."""

  def step(self, obs):
    super(Hallucination, self).step(obs)
    if _HAL_ARCHON in obs.observation["available_actions"]:
      player_relative = obs.observation["screen"][_PLAYER_RELATIVE]
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

