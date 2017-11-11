
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy 
from pysc2.agents import base_agent 
from pysc2.lib import features
from pysc2.lib import actions

_PLAYER_RELATIVE = features.SCREEN_FEATURES.player_relative.index
_PLAYER_FRIENDLY = 1
_PLAYER_HOSTILE = 4
_NO_OP = actions.FUNCTIONS.no_op.id
_MOVE_SCREEN = actions.FUNCTIONS.Move_screen.id
_ATTACK_SCREEN = actions.FUNCTIONS.Attack_screen.id
_SELECT_ARMY = actions.FUNCTIONS.select_army.id
_NOT_QUEUED = [0]
_SELECT_ALL = [0]
_FORCE_FIELD = actions.FUNCTIONS.Effect_ForceField_screen.id

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
  


class Sentry():
  '''Defines how the sentry SC2 unit works'''
  
  
  def Force_Field(sentry):
    '''Function related with Force Field creation'''
    _FORCE_FIELD = actions.FUNCTIONS.Effect_ForceField_screen.id

    
  def Guardian_Shield(sentry):
    '''Function related with Shield creation'''
    _GUARD_FIELD = actions.FUNCTIONS.Effect_GuardianShield_quick.id
  
  def Hallucinations(sentry):
    '''Functions related with Hallucination'''
    
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
    return actions.FunctionCall(actions.FUNCTIONS.no_op.id, [])
    
  def Standard_Functions(sentry):
    '''Standard Functions related with movements and exploration '''
  _NOOP = actions.FUNCTIONS.no_op.id
  _SELECT_POINT = actions.FUNCTIONS.select_point.id
  return actions.FunctionCall(actions.FUNCTIONS.no_op.id, [])


