import copy
import random

class Hat():

  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      for n in range(value):
        self.contents.append(key)
    
  def draw(self, num):
    balls = [] 
    if num > len(self.contents):
      for ball in self.contents:
        balls.append(ball)
        self.contents.remove(ball)
    else:
      for n in range(num):
        ball = random.choice(self.contents)
        balls.append(ball)
        self.contents.remove(ball)
    return balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  
  expected_list = []
  for key, value in expected_balls.items():
    for n in range(value):
      expected_list.append(key)
  
  M = 0
  N = num_experiments 

  for n in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    draw = hat_copy.draw(num_balls_drawn)
    match = 0
    for ball in set(expected_list):
      if draw.count(ball) >= expected_list.count(ball):
        match += 1
    if match == len(set(expected_list)):
      M += 1
  
  probability = M/N
  
  return probability

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat, expected_balls={"red":2,"green":1}, num_balls_drawn=5, num_experiments=2000)
print(probability)