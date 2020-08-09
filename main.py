class Coffee_Machine:
  n = 0
  water_in_machine = 400
  milk_in_machine = 540
  coffee_beans_in_machine = 120
  disposable_cups_in_machine = 9
  money_in_machine = 550
  espresso_water = 250
  espresso_coffee_beans = 16
  espresso_money = 4
  latte_water = 350
  latte_milk = 75
  latte_coffee_beans = 20
  latte_money = 7
  cappuccino_water = 200
  cappuccino_milk = 100
  cappuccino_coffee_beans = 12
  cappuccino_money = 6
  water_needed = 0
  milk_needed = 0
  coffee_beans_needed = 0
  money_earned = 0

  def __new__(cls):
    if cls.n == 0:
      cls.n += 1
      return object.__new__(cls)

  def print_machine_status(self):
    print("")
    print("The coffee machine has:")
    print(self.water_in_machine, "of water")
    print(self.milk_in_machine, "of milk")
    print(self.coffee_beans_in_machine, "of coffee beans")
    print(self.disposable_cups_in_machine, "of disposable cups")
    if self.money_in_machine > 0:
        print("$", self.money_in_machine, " of money", sep="")
    else:
        print(self.money_in_machine, " of money") 
    
  def resources_needed(self, coffee_type):
    if coffee_type == "1":
      self.water_needed = self.espresso_water
      self.milk_needed = 0
      self.coffee_beans_needed = self.espresso_coffee_beans
      self.money_earned = self.espresso_money
    elif coffee_type == "2":
      self.water_needed = self.latte_water
      self.milk_needed = self.latte_milk
      self.coffee_beans_needed = self.latte_coffee_beans
      self.money_earned = self.latte_money
    else:
      self.water_needed = self.cappuccino_water
      self.milk_needed = self.cappuccino_milk
      self.coffee_beans_needed = self.cappuccino_coffee_beans
      self.money_earned = self.cappuccino_money
    return self.water_needed, self.milk_needed, 

self.coffee_beans_needed, self.money_earned

  def buy_coffee(self, coffee_type):
      self.resources_needed(coffee_type)
      self.water_in_machine -= self.water_needed
      self.milk_in_machine -= self.milk_needed
      self.coffee_beans_in_machine -= self.coffee_beans_needed
      self.money_in_machine += self.money_earned
      self.disposable_cups_in_machine -= 1
      
  def check_resources(self, coffee_type):
    self.resources_needed(coffee_type)
    if (self.water_needed <= self.water_in_machine) and 

(self.milk_needed <= self.milk_in_machine) and 

(self.coffee_beans_needed <= self.coffee_beans_in_machine) and 

(self.disposable_cups_in_machine >= 1):
      print("I have enough resources, making you a coffee!")
      self.buy_coffee(coffee_type) 
    else:
      if self.water_needed > self.water_in_machine:
        print("Sorry, not enough water!")
      elif self.milk_needed > self.milk_in_machine:
        print("Sorry, not enough milk!")
      elif self.coffee_beans_needed > self.coffee_beans_in_machine:
        print("Sorry, not enough coffee beans!")
      else:
        print("Sorry, not enough disposable cups!")
      
  def fill(self):
      print("")
      print("Write how many ml of water do you want to add:")
      fill_water = int(input())
      self.water_in_machine += fill_water
      print("Write how many ml of milk do you want to add:")
      fill_milk = int(input())
      self.milk_in_machine += fill_milk
      print("Write how many grams of coffee beans do you want to 

add:")
      fill_coffee_beans = int(input())
      self.coffee_beans_in_machine += fill_coffee_beans
      print("Write how many disposable cups of coffee do you want 

to add:")
      fill_disposable_cups = int(input())
      self.disposable_cups_in_machine += fill_disposable_cups
      
  def take(self):
    self.money_in_machine
    print()
    print("I gave you $", self.money_in_machine, sep="")
    self.money_in_machine = 0
    
new_coffee_machine = Coffee_Machine()
print("Write action (buy, fill, take, remaining, exit):")
user_action = input()
while user_action != "exit":
  if user_action == "buy":
    print("")
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - 

cappuccino, back - to main menu:")
    user_coffee_type = input()
    if user_coffee_type == "1":
      new_coffee_machine.check_resources("1")
      print("")
      print("Write action (buy, fill, take, remaining, exit):")
      user_action = input()
            
    elif user_coffee_type == "2":
      new_coffee_machine.check_resources("2")
      print("")
      print("Write action (buy, fill, take, remaining, exit):")
      user_action = input()
        
    elif user_coffee_type == "3":
      new_coffee_machine.check_resources("3")
      print("")
      print("Write action (buy, fill, take, remaining, exit):")
      user_action = input()
            
    else:
      print("")
      print("Write action (buy, fill, take, remaining, exit):")
      user_action = input()
    
  elif user_action == "fill":
    new_coffee_machine.fill()
    print("")
    print("Write action (buy, fill, take, remaining, exit):")
    user_action = input()
  elif user_action == "take":
    new_coffee_machine.take()
    print("")
    print("Write action (buy, fill, take, remaining, exit):")
    user_action = input()
  elif user_action == "remaining":
    new_coffee_machine.print_machine_status()
    print("")
    print("Write action (buy, fill, take, remaining, exit):")
    user_action = input()
  else:
    break
                
