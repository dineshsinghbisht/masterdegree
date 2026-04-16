import random
import gymnasium as gym
import numpy as np
from collections import deque
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam


class DQNAgent:
    def __init__(self, state_size, action_size, TRAIN):
        self.state_size = state_size
        self.action_size = action_size

        # Replay memory stores past experiences for training
        self.memory = deque(maxlen=10000)

        self.gamma = 0.99           # discount rate
        self.epsilon = 1.0 if TRAIN else 0.0   # exploration rate
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.99
        self.learning_rate = 0.001
        self.model = self._build_model()

    def _build_model(self):
        # Neural Net for Deep-Q learning Model
        model = Sequential([
            Dense(32, activation='relu', input_shape=(self.state_size,)),
            Dense(32, activation='relu'),
            Dense(int(self.action_size), activation='linear')
        ])
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
        print('train')
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
    # Phase 1 - Training:  TRAIN=True,  LOAD=False, SAVE=True,  EPISODES=500
    # Phase 2 - Testing:   TRAIN=False, LOAD=True,  SAVE=False, EPISODES=10
    TRAIN    = True
    EPISODES = 500
    LOAD     = False
    SAVE     = True

    env = gym.make('CartPole-v1')
    state_size  = int(env.observation_space.shape[0])
    action_size = int(env.action_space.n)
    agent = DQNAgent(state_size, action_size, TRAIN)

    if LOAD:
        agent.load("weights.h5")

    done = False
    batch  = 300
    scores = deque(maxlen=3000)
    total  = 0
    mean   = 0

    for e in range(EPISODES):
        state = env.reset()
        state = state[0]
        state = np.reshape(state, [1, state_size])
        score = 0

        for time in range(300):
            if not TRAIN:
                env.render()
            action = agent.act(state)
            next_state, reward, done, _, _ = env.step(action)
            next_state = np.reshape(next_state, [1, state_size])
            agent.remember(state, action, reward, next_state, done)
            score += reward
            state = next_state
            if done or time == 299:
                scores.append(score)
                mean = sum(scores) / len(scores)
                print("episode: {}/{}, score: {:.5}, e: {:.2}, average: {:.5}"
                      .format(e, EPISODES, score, agent.epsilon, mean))
                if len(agent.memory) > 300:
                    if TRAIN:
                        agent.replay(batch, score)
                break

    if SAVE:
        agent.save("weights.h5")
        print("Weights saved!")

    env.close()