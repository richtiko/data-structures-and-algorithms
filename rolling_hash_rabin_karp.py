class RollingHash:
  def __init__(self):
    self.hash = 0
    self.base = 128
    self.prime = 999983
    self.power = 0;
    
  def append(self, char):
    self.hash = (self.hash*self.base + ord(char)) % self.prime
    self.power +=1
    
  def skip(self, char):
    self.hash = (self.hash - (ord(char)*((self.base**(self.power-1)) % self.prime) % self.prime) ) 
    self.power -= 1
    
  def get_hash(self):
    return self.hash

def search_for_string(to_find, where):
  indexes = []
  to_find_roling_hash = RollingHash()
  where_roling_hash = RollingHash()
  for i in to_find:
    to_find_roling_hash.append(i)
  
  for i in where[0:len(to_find)]:
    where_roling_hash.append(i)
    
  if where_roling_hash.get_hash() == to_find_roling_hash.get_hash():
    if where[0:len(to_find)] == to_find:
      #print("found at index 0")
      indexes.append(0)
      
  for i in range(len(to_find), len(where)):
    where_roling_hash.skip(where[i-len(to_find)])
    where_roling_hash.append(where[i])
    if where_roling_hash.get_hash() == to_find_roling_hash.get_hash():
      if where[i-len(to_find)+1: i+1] == to_find:
        #print("found at index ",i-len(to_find)+1)
        indexes.append(i-len(to_find)+1)
  return indexes
    
  
indexes = search_for_string("abc","abcaasdfghabcjklqwabc")
if indexes != [0, 10 ,18]:
  raise RuntimeError("found not expected indexes", indexes)
print("OK")
