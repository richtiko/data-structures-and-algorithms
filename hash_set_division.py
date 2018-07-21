from hash_set import HashSetBase

class HashSetDiv(HashSetBase):
  
  def __init__(self):
    print("creating HashSetDiv")
    HashSetBase.__init__(self, 7001)

  def compute_hash(self, number):
    return number % self.length
    

    
    
    
  
