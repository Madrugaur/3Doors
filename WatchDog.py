import json

class WatchDog:
  def __init__(self):
    self.tracking = dict()
    
    
  def __str__(self):
    return json.dumps(self.tracking, default=lambda o: o.tracking)
  
  def __repr__(self) -> str:
    return self.__str__()
  def track(self, key: str, init: int = 0):
    self.tracking[key] = init
  
  def pack(self, key: str, dog):
    self.tracking[key] = dog
  
  def under(self, key: str) -> "WatchDog":
    return self.tracking[key]
  
  def trackingList(self):
    return list(self.tracking.keys())
  
  def report(self):
    return self.tracking
  
  def inc(self, key: str):
    self.tracking[key] += 1
  
  def dec(self, key: str):
    self.tracking[key] -= 1
  
  def set(self, key: str, val: int):
    self.tracking[key] = val
    
  def get(self, key: str):
    return self.tracking[key]
      