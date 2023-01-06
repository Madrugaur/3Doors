from enum import Enum
from random import shuffle


class Possibilities(Enum):
    CAR = 1
    NOTHING = 2
    GOAT = 3
  
    Possibilities = [CAR, NOTHING, GOAT]

def permute():
  ls = [Possibilities.CAR, Possibilities.GOAT, Possibilities.NOTHING]
  shuffle(ls)
  return ls