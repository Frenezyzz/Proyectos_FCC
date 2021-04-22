import math
class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"
    
  
  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height
    
  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    shape = ""
    row = 0
    
    if self.width <= 50 and self.height <= 50:
      
      while row < self.height:
        shape += "*"*self.width + "\n"
        row += 1

      return shape
    else:
      return "Too big for picture."
    

  def get_amount_inside(self, figure):
    main_figure = self.height * self.width
    second_figure = figure.height * figure.width
    result = main_figure / second_figure

    print(f"main {main_figure} - {second_figure}")
    if result == int:
      return result
    elif result != int:
      return math.floor(result)
    else:
      return 0
      


class Square(Rectangle):
  def __init__(self, side):
    self.width = side
    self.side = side
    self.height = side
    
  def __str__(self):
    return f"Square(side={self.side})"


  def set_width(self, width):
    self.side = width 

  def set_height(self, height):
    self.side = height

  def set_side(self,side):
    self.side = side
    self.height = side
    self.width = side


