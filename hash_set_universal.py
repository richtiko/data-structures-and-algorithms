import sys
import random
from hash_set import HashSetBase

class HashSetUni(HashSetBase):
  
  def __init__(self):
    print("creating HashSetUni")
    self.big_prime = 179426549
    self.a = random.randint(1, self.big_prime - 1)
    self.b = random.randint(0, self.big_prime - 1)
    
    HashSetBase.__init__(self, 10)
      
  def compute_hash(self, number):
    return (self.a * number + self.b) % self.big_prime % self.length
  
  def get_shrink_length(self, current_length):
    return int(current_length/2) + 1
  
  def get_double_length(self, current_length):
    return int(current_length*2)

    
    
    
  
