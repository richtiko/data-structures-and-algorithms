import sys

class HashSetBase:
  
  class node:
    def __init__(self, value = None):
      self.value = value
      self.next = None

  def __init__(self, length):

    self.longest_chain = 0
    self.length = length
    self.number_of_elements = 0
    self.table = []
    for i in range(0, self.length):
      self.table.append(HashSetBase.node())
      
  def get_longest_chain(self):
    return self.longest_chain;
  
  def compute_hash(self, number):
    raise RuntimeError("not implemented")

  def double_table(self):
    self.length = self.get_double_length(self.length)
    self.number_of_elements = 0
    old_table = self.table
    self.table = []
    for i in range(0, self.length):
      self.table.append(HashSetBase.node())
    self.insert_old_table(old_table)

  def shrink_table(self):
    self.length = self.get_shrink_length(self.length)
    self.number_of_elements = 0
    old_table = self.table
    self.table = []
    for i in range(0, self.length):
      self.table.append(HashSetBase.node())
    self.insert_old_table(old_table)
    
  def insert_old_table(self, old_table):
    for list_head in old_table:
      node = list_head
      while node != None and node.value != None:
        self.insert(node.value)
        node = node.next
    
    
  def insert(self, number):
    if self.number_of_elements + 1 > self.length:
      self.double_table(); 
    index = self.compute_hash(number)
    node = self.table[index]
    chain_length = 1
    #to check for existing element we go to the end of the list, if no existing element were to be submitted we sould insert node to the beginning
    while node.next != None and node.value != number:
      node = node.next
      chain_length += 1
    if node.value == number:
      return
    if node.value == None:
      node.value = number
    else:
      node.next = HashSetBase.node(number)
      chain_length += 1
    if chain_length > self.longest_chain:
      self.longest_chain = chain_length
    self.number_of_elements += 1

  def find(self, number):
    index = self.compute_hash(number)
    node = self.table[index]
    while node != None and node.value != number:
      node = node.next
    return node != None
  
  def delete(self, number):
    if self.number_of_elements - 1 < self.length/4:
      self.shrink_table(); 
    index = self.compute_hash(number)
    node = self.table[index]
    prev = None
    while node != None and node.value != number:
      prev = node
      node = node.next
    if node != None:
      if prev != None:# it is not the first node in the chain
        #print("removing not head of list ",node.value)
        prev.next = node.next
        del node
      else:#first node in the chain
        #print("removing head of list ",node.value)
        node.value = None
        if node.next != None:
          #print("removing head of list not only")
          #copy next element to this slotand remove next node instead
          to_delete = node.next
          node.value = node.next.value
          node.next = node.next.next
          del to_delete
      self.number_of_elements -= 1 
    

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

    
    
    
  
