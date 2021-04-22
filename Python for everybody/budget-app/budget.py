

class Category:
  
  def __init__(self, name):
        self.name = name
        self.ledger = []
        self.cash_start = 0
  
  def __str__(self):
    characters = 30
    budget = ""
    title = 0
    total = 0

    title = characters - len(self.name)
    title /= 2
    budget = "*"*round(title) + self.name + "*"*round(title)

    for obj in self.ledger:
      
      budget += f"\n{obj['description'][0:23]:23}" + f"{obj['amount']:>7.2f}"

      total += obj["amount"]
  

    budget += f"\nTotal: {total}"  

    return budget


  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})
    self.cash_start = amount
  
  def withdraw(self,amount, description=""):
    if self.check_funds(amount):    
      self.ledger.append({"amount": -amount, "description": description})
      return True
    return False

  def get_balance(self):
    balance = 0
    for item in self.ledger:
      balance += item["amount"]
    return balance 

  def transfer(self,amount, category):
    if self.check_funds(amount):
      self.withdraw(amount,"Transfer to " + category.name)
      category.deposit(amount, "Transfer from " + self.name)
      return True
    return False
  
  def check_funds(self, amount):
    if self.get_balance() >= amount:
      return True
    return False

  def get_withdrawls(self):
    total = 0
    for item in self.ledger:
      if item["amount"] < 0:
        total += item["amount"]
    return total


def truncate(number):
  mult = 10
  return int(number * mult) / mult

def get_total(categories):
  total = 0
  porcentaje = []

  for item in categories: #itera por cada categoria
    total += item.get_withdrawls() # total gastado en la categoria
    porcentaje.append(item.get_withdrawls()) #guarda el total
  result = list(map(lambda x: truncate(x/total),porcentaje)) #iteracion 

  return result

def create_spend_chart(categories):
  title = "Percentage spent by category\n"
  i = 100
  totals = get_total(categories)
  while i >= 0 :
    spaces = " "
    for total in totals:
      if total * 100 >= i:
        spaces += "o  "
      else:
        spaces += "   "
    title += str(i).rjust(3) +"|" + spaces + ("\n")
    i-=10
  
  mid_scores = "-" + "---"*len(categories)
  names = []
  x_eje = ""
  for item in categories:
    names.append(item.name)
  
  maximo = max(names, key=len)

  for x in range(len(maximo)):
    name_string = "     "         #critico
    for name in names:
      if x >= len(name):
        name_string += "   "
      else:
        name_string += name[x] + "  "
    
    if (x != len(maximo) - 1):
      name_string += '\n'
    

    x_eje += name_string
  title += mid_scores.rjust(len(mid_scores)+4) + "\n" + x_eje
  return title