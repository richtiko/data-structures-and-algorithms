import sys
from hash_set_multipication import HashSetMul
from hash_set_division import HashSetDiv
from hash_set_universal import HashSetUni
import random

hashsets =[]
hashsets.append(HashSetMul())
hashsets.append(HashSetDiv())
hashsets.append(HashSetUni())
for hashset in hashsets:
  
  array = []
  for i in range(0,20000):
    array.append(random.randint(1,1000000))
    hashset.insert(array[i])

  print("longest_chain=",hashset.get_longest_chain())
  for a in array:
    if hashset.find(a) == False:
      raise RuntimeError ("can not find ", a)

  for a in array:
    hashset.delete(a)
    if hashset.find(a) == True:
      raise RuntimeError ("did not remove ", a)

  if hashset.empty() == False:
    raise RuntimeError ("is not empty")

  print("OK")



    
    
    
  
