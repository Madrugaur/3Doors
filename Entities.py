from Possibilities import Possibilities
from Outcome import Outcome
import random

class GameStage:
  def __init__(self, doors):
    self.doors = doors    
    self.indexOfNothing = -1
    for i in range(0, len(doors)):
      if doors[i] == Possibilities.NOTHING:
        self.indexOfNothing = i
    
    self.validDoors = [*range(0, 3)]
  
  def getOptions(self):
    return self.validDoors

  def removeNothingDoor(self):
    self.validDoors.remove(self.indexOfNothing)
  
  def reveal(self, index):
    return self.doors[index]
  
  
  

class GameHost:  
  def __init__(self, doors, second_chance):
    self.doors = doors
    self.second_chance = second_chance

    self.stage = GameStage(doors)
    self.firstGuess = True
    
  def submit(self, player_guess: int):
    result = self.stage.reveal(player_guess)
    
    if (result == Possibilities.NOTHING): return Outcome.INCORRECT
  
    if (result == Possibilities.CAR): return Outcome.CORRECT
    
    if (not self.firstGuess or not self.second_chance): return Outcome.INCORRECT
    
    self.firstGuess = False
    self.stage.removeNothingDoor()
    return Outcome.GUESS_AGAIN
  
  def getOptions(self):
    return self.stage.getOptions()

class Player:
  def __init__(self, switch_guess, options):
    self.switch_guess = switch_guess
    self.options = options
    
    self.firstGuess = True
    
  def makeGuess(self):
    guess = random.randint(0, len(self.options) - 1)
    if self.firstGuess:
      self.guess = guess
      self.firstGuess = False
      return guess
    
    if not self.firstGuess and self.switch_guess:
      switched_guess = (self.options.index(self.guess) + 1) % len(self.options)
      return self.options[switched_guess]
    else:
      return self.guess
  
  def updateOptions(self, newOptions):
    self.options = newOptions