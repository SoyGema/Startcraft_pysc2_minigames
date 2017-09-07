
from pysc2.agents import base_agents
from pysc2.lib import actions


## SENTINEL FUNCTIONS

# Functions related with Hallucination

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

# Functions 
_NOOP = actions.FUNCTIONS.no_op.id
_SELECT_POINT = actions.FUNCTIONS.select_point.id

# Functions related with attack 
