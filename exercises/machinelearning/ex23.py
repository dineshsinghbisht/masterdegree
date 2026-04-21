# -*- coding: utf-8 -*-
import os
import random
import gymnasium as gym
import numpy as np
from collections import deque
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.layers import LeakyReLU
from tensorflow.keras.optimizers import Adam


#%%

class DQNAgent:
    def __init__(self, state_size, action_size, TRAIN, start_epsilon=1.0):
        self.state_size = state_size
        self.action_size = action_size
        self.memory = deque(maxlen=10000)
        self.gamma = 0.99    # discount rate
        if TRAIN:
            self.epsilon = start_epsilon
        else:
            self.epsilon = 0.0
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.learning_rate = 0.001
        self.model = self._build_model()

    def _build_model(self):
        model = Sequential()
        model.add(Input(shape=(self.state_size,)))
        model.add(Dense(64))
        model.add(LeakyReLU(negative_slope=0.1))
        model.add(Dense(64))
        model.add(LeakyReLU(negative_slope=0.1))
        model.add(Dense(self.action_size, activation='linear'))
        model.compile(loss='mse', optimizer=Adam(learning_rate=self.learning_rate))
        return model

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state):
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)
        act_values = self.model.predict(state, verbose=0)
        return np.argmax(act_values[0])

    def replay(self, batch, score):
        minibatch = random.sample(self.memory, batch)
        states = []
        rewards = []
        for state, action, reward, next_state, done in minibatch:
            target = reward
            if not done:
                target = (reward + self.gamma * np.amax(self.model.predict(next_state, verbose=0)[0]))
            target_f = self.model.predict(state, verbose=0)
            target_f[0][action] = target
            states = np.append(states, state)
            rewards = np.append(rewards, target_f[0])
        self.model.fit(states.reshape(batch, self.state_size),
                       rewards.reshape(batch, self.action_size),
                       epochs=5, batch_size=25, verbose=0)
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def load(self, name):
        self.model.load_weights(name)

    def save(self, name):
        self.model.save_weights(name)


if __name__ == "__main__":
    # Phase 1: set TRAIN=True, LOAD=False, SAVE=True  -> trains and saves weights
    # Phase 2: set TRAIN=False, LOAD=True, SAVE=False -> loads weights and records video
    # TRAIN = True
    TRAIN = False
    EPISODES = 1
    LOAD = True
    SAVE = False
    START_EPSILON = 0.0

    weights_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "weights.weights.h5")
    video_dir = os.path.dirname(os.path.abspath(__file__))

    render_mode = "rgb_array" if not TRAIN else None
    env = gym.make('CartPole-v1', render_mode=render_mode)

    if not TRAIN:
        env = gym.wrappers.RecordVideo(env, video_folder=video_dir,
                                       episode_trigger=lambda _: True,
                                       video_length=0,
                                       name_prefix="ex23")

    state_size = int(env.observation_space.shape[0])
    action_size = int(env.action_space.n)
    agent = DQNAgent(state_size, action_size, TRAIN, start_epsilon=START_EPSILON if LOAD else 1.0)

    if LOAD:
        agent.load(weights_file)

    batch = 32
    scores = deque(maxlen=100)

    for e in range(EPISODES):
        state = env.reset()
        state = state[0]
        state = np.reshape(state, [1, state_size])
        score = 0
        for time in range(300):
            action = agent.act(state)
            next_state, reward, done, _, _ = env.step(action)
            next_state = np.reshape(next_state, [1, state_size])
            agent.remember(state, action, reward, next_state, done)
            score += reward
            state = next_state
            if done or time == 299:
                scores.append(score)
                mean = sum(scores) / len(scores)
                print("episode: {}/{}, score: {:.5}, e: {:.3}, average(100): {:.5}"
                      .format(e, EPISODES, score, agent.epsilon, mean))
                if len(agent.memory) > 300 and TRAIN:
                    agent.replay(batch, score)
                break

    if SAVE:
        agent.save(weights_file)

    env.close()
