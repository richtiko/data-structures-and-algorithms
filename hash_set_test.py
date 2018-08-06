import sys
from hash_set_multipication import HashSetMul
from hash_set_division import HashSetDiv
from hash_set_division import HashSetInPlaceDiv
from hash_set_universal import HashSetUni

import random

hashsets =[]

hashsets.append(HashSetDiv())
hashsets.append(HashSetMul())
hashsets.append(HashSetUni())
hashsets.append(HashSetInPlaceDiv())

for hashset in hashsets:
  
  array = []
  for i in range(0,20000):#20000
    array.append(random.randint(1,1000000))
    hashset.insert(array[i])

  array = list(set(array))
  random.shuffle(array)
  
  print("longest_chain=",hashset.get_longest_chain())
  for a in array:
    if hashset.find(a) == False:
      raise RuntimeError ("can not find ", a)

  print("removing half the elements")
  for a in array[0:int(len(array)/2)]:
    hashset.delete(a)
    if hashset.find(a) == True:
      raise RuntimeError ("did not remove ", a)
    array.remove(a)
    
##    ##for debugging
##    for b in array:
##      if hashset.find(b) == False:
##        raise RuntimeError ("can not find ", b)


  for a in array:
    if hashset.find(a) == False:
      raise RuntimeError ("can not find ", a)

  print("removing rest of the elements", len(array))
  for a in array:
    hashset.delete(a)
    if hashset.find(a) == True: 
      raise RuntimeError ("did not remove ", a)

  if hashset.empty() == False:
    raise RuntimeError ("is not empty")

  print("OK")



    
    
    
  
