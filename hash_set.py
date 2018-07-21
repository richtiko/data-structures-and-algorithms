import sys

class HashSetBase:
  
  class node:
    def __init__(self, value = None):
      self.value = value
      self.next = None

  def __init__(self, length):

    self.longest_chain = 0
    self.length = length
    self.table = []
    for i in range(0, self.length):
      self.table.append(HashSetBase.node())
      
  def get_longest_chain(self):
    return self.longest_chain;
  
  def compute_hash(self, number):
    raise RuntimeError("not implemented")
    
  def insert(self, number):
    index = self.compute_hash(number)
    node = self.table[index]
    chain_length = 1
    while node.next != None:
      node = node.next
      chain_length += 1
    if node.value == None:
      node.value = number
    else:
      node.next = HashSetBase.node(number)
      chain_length += 1
    if chain_length > self.longest_chain:
      self.longest_chain = chain_length
    

  def find(self, number):
    index = self.compute_hash(number)
    node = self.table[index]
    while node != None and node.value != number:
      node = node.next
    return node != None
  
  def delete(self, number):
    index = self.compute_hash(number)
    node = self.table[index]
    prev = None
    while node != None and node.value != number:
      prev = node
      node = node.next
    if node != None:
      if prev != None:# it is not the first node in the chain
        del node
        prev.next = None
      else:#first node in the chain
        node.value = None
        node.next = None

  def empty(self):
    for node in self.table:
      if node.value != None or node.next != None:
        return False
    return True
    

##import random
##hashset = HashSet()
##array = []
##for i in range(0,20000):
##  array.append(random.randint(1,1000000))
##  hashset.insert(array[i])
##
##print("longest_chain=",hashset.get_longest_chain())
##for a in array:
##  if hashset.find(a) == False:
##    raise RuntimeError ("can not find ", a)
##
##for a in array:
##  hashset.delete(a)
##  if hashset.find(a) == True:
##    raise RuntimeError ("did not remove ", a)
##
##if hashset.empty() == False:
##  raise RuntimeError ("is not empty")
##
##print("OK")

    
    
    
  
