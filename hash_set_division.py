from hash_set import HashSetBase
from hash_set_in_place_allocation import HashSetBaseInPlace

class HashSetDiv(HashSetBase):
  
  def __init__(self):
    print("creating HashSetDiv")
    HashSetBase.__init__(self, 7001)

  def compute_hash(self, number):
    return number % self.length
    
class HashSetInPlaceDiv(HashSetBaseInPlace):
  
  def __init__(self):
    print("creating HashSetInPlaceDiv")
    HashSetBaseInPlace.__init__(self, 20011)#

  def compute_hash(self, number):
    return number % self.length

    
    
    
  
