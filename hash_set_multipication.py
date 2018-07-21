import sys
from hash_set import HashSetBase

class HashSetMul(HashSetBase):
  
  def __init__(self):
    print("creating HashSetMul")
    self.power = 13
    HashSetBase.__init__(self, 2**self.power)
      
  def compute_hash(self, number):
    K_S = 2654435769 * number
    mask = 0xFFFFFFFF
    lower_32_bits = K_S & mask
    return lower_32_bits >> (32 - self.power)    


    
    
    
  
