#SC2-pySC2 agent for HallucinIce mini-game
#@SoyGema
#Thanks to @DavSuCar


import numpy as np
import sys
import random
import time

from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, Activation, MaxPooling2D, TimeDistributed, LSTM, Reshape
from keras.optimizers import Adam, Adamax, Nadam
from keras.backend import set_image_dim_ordering
from absl import flags

from pysc2.env import sc2_env
from pysc2.env import environment as pysc2environment
from pysc2.lib import actions
from pysc2.lib import features

from rl.memory import SequentialMemory
from rl.policy import LinearAnnealedPolicy, EpsGreedyQPolicy
from rl.core import Processor
from rl.callbacks import FileLogger, ModelIntervalCheckpoint
from rl.agents.dqn import DQNAgent
# from rl.agents.sarsa import SARSAAgent

# Actions from pySC2 API

FUNCTIONS = actions.FUNCTIONS
_PLAYER_RELATIVE = features.SCREEN_FEATURES.player_relative.index
_PLAYER_FRIENDLY = 1
_PLAYER_NEUTRAL = 3
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

# Size of the screen and length of the window

_WINDOW_LENGTH = 1

# Load and save weights for training

LOAD_MODEL = False  # True if the training process is already created
SAVE_MODEL = True

# Configure Flags for executing model from console:

FLAGS = flags.FLAGS
flags.DEFINE_string("mini_game", "HallucinIce", "Name of the minigame.")
flags.DEFINE_integer("screen_size", "64", "Resolution for screen actions.")
flags.DEFINE_integer("minimap_size", "32", "Resolution for minimap actions.")
# flags.DEFINE_string("algorithm", "deepq", "RL algorithm to use")
flags.DEFINE_bool("verbose", False, "Intended to help a programmer read actions taken in real-time.")
flags.DEFINE_float("pause", 0.0, "Seconds to pause between consecutive actions. Intended to help a programmer observe the effect of an action taken in real-time.")
flags.DEFINE_bool("visualize", True, "Visualize game")
flags.DEFINE_integer("steps_per_ep", 150, "steps per episode.")
FLAGS(sys.argv)

# Processor

class SC2Proc(Processor):
    def process_observation(self, observation):
        """Process the observation as obtained from the environment for use an agent and returns it"""
        obs = observation[0].observation["feature_screen"][_PLAYER_RELATIVE]
        return np.expand_dims(obs, axis=2)

    def process_state_batch(self, batch):
        """Processes an entire batch of states and returns it"""
        batch = np.swapaxes(batch, 0, 1)
        return batch[0]

#  Define the environment

class Environment(sc2_env.SC2Env):
    """Starcraft II environmet. Implementation details in lib/features.py"""

    def __init__(self):
        # Creates common pysc2 objects required for running of agent.
        agent_interface_format=features.AgentInterfaceFormat(
                            feature_dimensions=features.Dimensions(screen=FLAGS.screen_size, minimap=FLAGS.minimap_size))
        feats = features.Features(agent_interface_format)
        action_spec = feats.action_spec()
        super().__init__(map_name=FLAGS.mini_game, 
                        visualize=FLAGS.visualize, 
                        game_steps_per_episode=FLAGS.steps_per_ep,
                        agent_interface_format=agent_interface_format)
        # Save variables which can help in debugging or better unds-ing pysc2:
        self.observation_spec = self.observation_spec()
        self.agent_interface_format = agent_interface_format
        self.feats = feats
        self.action_spec = action_spec
        # Initialize variables:
        self.episode_reward = 0
        self.observation_cur = None

    def step(self, action):
        """Apply actions, step the world forward, and return observations"""        
        if FLAGS.verbose:
            print('{} AVAILABLE ACTIONS.'.format(len(self.observation_cur.available_actions)))
            # Uncomment to print individual available actions.
            # for a in observation_cur.available_actions:
            #     print(actions.FUNCTIONS[a])

        chosen_func_id = np.random.choice(self.observation_cur.available_actions)

        if FLAGS.verbose:
            chosen_action = actions.FUNCTIONS[chosen_func_id]  
            print('Chosen action: ', chosen_func_id, '~~', chosen_action)
        
        # Uncomment to print "template" args of chosen action:
        # allargs = self.action_spec.functions[chosen_func_id].args
        # for arg in allargs:
        #     print(arg); print('arg sizes ', arg.sizes)
        
        chosen_args = [[np.random.randint(0, size) for size in arg.sizes] for arg in self.action_spec.functions[chosen_func_id].args]

        if FLAGS.verbose:
            print('Chosen args: ', chosen_args)

        action = actions.FunctionCall(chosen_func_id, chosen_args)
        obs = super(Environment, self).step([action])
        self.observation_cur = obs[0].observation
        r = obs[0].reward
        done = obs[0].step_type == pysc2environment.StepType.LAST
        self.episode_reward += r
        time.sleep(FLAGS.pause)
        return obs, r, done, {}

    def reset(self):
        obs = super(Environment, self).reset()
        self.observation_cur = obs[0].observation
        self.episode_reward = 0
        return obs

def actions_to_choose():
    hall = [_HAL_ADEPT, _HAL_ARCHON, _HAL_COL, _HAL_DISRUP,
            _HAL_HIGTEM, _HAL_IMN, _HAL_PHOENIX, _HAL_STALKER,
            _HAL_VOIDRAID, _HAL_ZEALOT, _FORCE_FIELD, _GUARD_FIELD]
    action = actions.FunctionCall(_HAL_ADEPT, [_NOT_QUEUED])
    print(action)
    return action

# TO-DO : Define actions_to_choose based on SC2 sentry unit

# Agent architecture using keras rl

def neural_network_model(input, actions):
    model = Sequential()
    # Define CNN model
    print(input)
    model.add(Conv2D(256, kernel_size=(5, 5), input_shape=input))
    model.add(MaxPooling2D(pool_size=(2, 2), strides=None, padding='valid', data_format=None))
    model.add(Flatten())

    model.add(Dense(256, activation='relu'))
    model.add(Reshape((1, 256)))

    model.add(LSTM(256))
    model.add(Dense(actions, activation='softmax'))
    model.summary()
    model.compile(loss="categorical_crossentropy",
                  optimizer="adam",
                  metrics=["accuracy"])

    return model


def training_game():
    env = Environment()

    input_shape = (FLAGS.screen_size, FLAGS.screen_size, 1)
    nb_actions = 12  # Number of actions

    model = neural_network_model(input_shape, nb_actions)
    memory = SequentialMemory(limit=5000, window_length=_WINDOW_LENGTH)

    processor = SC2Proc()

    # Policy

    policy = LinearAnnealedPolicy(EpsGreedyQPolicy(), attr="eps", value_max=1, value_min=0.7, value_test=.0, nb_steps=1e6)

    # Agent

    dqn = DQNAgent(model=model, 
                    nb_actions=nb_actions, 
                    memory=memory, 
                    enable_double_dqn=False,
                    nb_steps_warmup=500, 
                    # nb_steps_warmup=1, 
                    target_model_update=1e-2, 
                    policy=policy,
                    batch_size=150,
                    processor=processor)

    dqn.compile(Adam(lr=.001), metrics=["mae"])

    # Tensorboard callback

    callbacks = keras.callbacks.TensorBoard(log_dir='./Graph', histogram_freq=0,
                                write_graph=True, write_images=False)
    
    
    # Save the parameters and upload them when needed

    name = FLAGS.mini_game
    w_file = "dqn_{}_weights.h5f".format(name)
    check_w_file = "train_w" + name + "_weights.h5f"

    if SAVE_MODEL:
        check_w_file = "train_w" + name + "_weights_{step}.h5f"

    log_file = "training_w_{}_log.json".format(name)

    if LOAD_MODEL:
        dqn.load_weights(w_file)

    dqn.fit(env, callbacks=callbacks, nb_steps=1e7, action_repetition=2,
            log_interval=1e4, verbose=2)

    dqn.save_weights(w_file, overwrite=True)
    dqn.test(env, action_repetition=2, nb_episodes=30, visualize=False)


if __name__ == '__main__':
    print('FLAGS:')
    for k in FLAGS._flags():
        print(k, FLAGS[k].value)
    print('-'*20)
    training_game()
