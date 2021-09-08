import gym
import random

env = gym.make("CartPole-v1")
print(env.observation_space)
print(env.action_space)
observation = env.reset()


class Agent():
    def __init__(self, env):
      self.action_size = env.action_space.n
      print(self.action_size)

    def get_action(self):
      #action = random.choice(range(self.action_size))
      pole_angle = state[2]
      action = 0 if pole_angle<0 else 1
      return action


agent = Agent(env)
state = env.reset()

for _ in range(200):
  env.render()
  #action = env.action_space.sample() # your agent here (this takes random actions)
  action = agent.get_action()
  state, reward ,done, info= env.step(action)
  # #observation, reward, done, info = env.step(action)
  # if done:
  #   observation = env.reset()
env.close()