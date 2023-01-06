
import argparse
import sys
import Possibilities
from Outcome import Outcome
from Entities import GameStage, GameHost, Player
from WatchDog import WatchDog
from tqdm import tqdm
def generateDoors():
  return Possibilities.permute()

def simulate(watchDog: WatchDog, switch_guess: bool, host_give_second_chance: bool):
  doors = generateDoors()
  
  host = GameHost(doors, host_give_second_chance)
  player = Player(switch_guess, host.getOptions())
  
  guess = player.makeGuess()
  
  res = host.submit(guess)
  
  if (res == Outcome.CORRECT):
    watchDog.under("player").inc("correct")
    return

  if (res == Outcome.INCORRECT):
    return
  
  player.updateOptions(host.getOptions())
  guess = player.makeGuess()
    
  res = host.submit(guess)
  
  if (res == Outcome.CORRECT):
    watchDog.under("player").inc("correct")
    return

  if (res == Outcome.INCORRECT):
    return
  
  print("NEVER SHOULD PRINT ME!!!")


def main():
  watchDog = WatchDog()
  
  simulations_to_run = 1_000_000
  
  run1Dog = WatchDog()
  run1Dog.pack("player", WatchDog())
  run1Dog.under("player").track("correct")
  
  run2Dog = WatchDog()
  run2Dog.pack("player", WatchDog())
  run2Dog.under("player").track("correct")
  
  run3Dog = WatchDog()
  run3Dog.pack("player", WatchDog())
  run3Dog.under("player").track("correct")
   
  run4Dog = WatchDog()
  run4Dog.pack("player", WatchDog())
  run4Dog.under("player").track("correct")
  
  watchDog.pack("run1", run1Dog)
  watchDog.pack("run2", run2Dog)
  watchDog.pack("run3", run3Dog)
  watchDog.pack("run3", run4Dog)

  
  for i in tqdm(range(0, simulations_to_run), unit="runs"):
    simulate(run1Dog, False, True)
  
  for i in tqdm(range(0, simulations_to_run),  unit="runs"):

    simulate(run2Dog, False, False)
  
  for i in tqdm(range(0, simulations_to_run),  unit="runs"):
    simulate(run3Dog, True, True)
    
  for i in tqdm(range(0, simulations_to_run),  unit="runs"):
    simulate(run4Dog, True, False)
    
  run1Ratio: float = run1Dog.under("player").get("correct") / simulations_to_run  
  run2Ratio: float = run2Dog.under("player").get("correct") / simulations_to_run  
  run3Ratio: float = run3Dog.under("player").get("correct") / simulations_to_run  
  run4Ratio: float = run4Dog.under("player").get("correct") / simulations_to_run  

  print(f"\n\n## Results ##\nRuns per Trial: {simulations_to_run}\n")

  print(f"Trail 1:\n\tSwitch Guess: False, Second Chance: True\n\tResult => {run1Ratio}")
  print(f"Trail 2:\n\tSwitch Guess: False, Second Chance: False\n\tResult => {run2Ratio}")
  print(f"Trail 3:\n\tSwitch Guess: True,  Second Chance: True\n\tResult => {run3Ratio}")
  print(f"Trail 4:\n\tSwitch Guess: True,  Second Chance: False\n\tResult => {run4Ratio}")



if __name__ == "__main__":
  main()