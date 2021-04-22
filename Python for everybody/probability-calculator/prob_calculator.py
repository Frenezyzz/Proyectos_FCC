import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self,**kwargs):
    self.contents = []

    for key, value in kwargs.items():
      for i in range(value):
        self.contents.append(key)
    
  
  def draw(self, to_draw):
    if to_draw > len(self.contents):
      return self.contents
    
    balls_removed = []
    for i in range(to_draw):
      random_ball = self.contents.pop(int(random.random() * len(self.contents)))
      balls_removed.append(random_ball)
                  
    return balls_removed




def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count = 0
  for i in range(num_experiments):
    expected_balls_copy = copy.deepcopy(expected_balls)
    hat_copy = copy.deepcopy(hat)
    colors_gotten = hat_copy.draw(num_balls_drawn)

    for color in colors_gotten:
      if color in expected_balls_copy:
        expected_balls_copy[color] -= 1
    
    if (all(x <= 0 for x in expected_balls_copy.values())):
      count +=1

    
  return count / num_experiments