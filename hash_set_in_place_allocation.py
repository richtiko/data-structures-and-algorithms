import sys

class HashSetBaseInPlace:
  
  class node:
    def __init__(self, value = None):
      self.prev_or_value = value
      self.next = None
      self.is_free = True

  def __init__(self, length):

    self.longest_chain = 0
    self.length = length
    self.table = []
    self.free_list = None
    for i in range(0, self.length): 
      self.table.append(HashSetBaseInPlace.node())
    for i in range(0, self.length): 
      self.add_to_free(self.table[i]);
      
  def add_to_free(self, node):
    node.is_free = True
    node.prev_or_value = None
    node.next = self.free_list
    if self.free_list != None:
      self.free_list.prev_or_value = node
    self.free_list = node
  
  def remove_from_free(self, node):
    node.is_free = False
    if node.prev_or_value != None:
      node.prev_or_value.next = node.next
    if node.next != None:
      node.next.prev_or_value = node.prev_or_value
    if node == self.free_list:
      self.free_list = node.next
    node.next = None
    node.prev_or_value = None

  def get_free_node(self):
    if self.free_list == None:
      raise RuntimeError("no free space")
    node = self.free_list
    self.remove_from_free(node)
    return node
    
  def get_longest_chain(self):
    return self.longest_chain;
  
  def compute_hash(self, number):
    raise RuntimeError("not implemented")
    
  def insert(self, number):
    index = self.compute_hash(number)
    node = self.table[index]
    
    if node.is_free:
      self.remove_from_free(node)
      node.is_free = False
      node.prev_or_value = number
      node.next = None
      if 1 > self.longest_chain:
        self.longest_chain = 1
      return
    if self.compute_hash(node.prev_or_value) != index:
      #if head of the list has a different hash we ned to reallocate it
      #then place number in current node
      [prev, node] = self.find_node(node.prev_or_value)
      #print("replacing",node.prev_or_value,"prev = ",prev.prev_or_value)
      new_node = self.get_free_node()
      new_node.is_free = False
      new_node.prev_or_value = node.prev_or_value
      new_node.next = node.next
      prev.next = new_node
      node.next = None
      node.prev_or_value = number
      return
    chain_length = 1
    while node.next != None and node.prev_or_value != number:
      node = node.next
      chain_length += 1
    if node.prev_or_value == number:
      return
    node.next = self.get_free_node()
    node = node.next
    node.is_free = False
    node.prev_or_value = number
    node.next = None
    chain_length += 1
    if chain_length > self.longest_chain:
      self.longest_chain = chain_length
    
  def find_node(self, number):
    index = self.compute_hash(number)
    node = self.table[index]
    prev = None
    while node != None and node.prev_or_value != number and node.is_free == False:
      prev = node
      node = node.next
    return [prev, node]
  
  def find(self, number):
##    index = self.compute_hash(number)
##    node = self.table[index]
##    while node != None and node.prev_or_value != number and node.is_free == False:
##      node = node.next
    [prev, node] = self.find_node(number)
    return node != None and node.is_free == False
  
  def delete(self, number):
##    index = self.compute_hash(number)
##    node = self.table[index]
##    prev = None
##    while node != None and node.prev_or_value != number and node.is_free == False:
##      prev = node
##      node = node.next
    [prev, node] = self.find_node(number)
    if node != None:
      if prev != None:# it is not the first node in the chain
        #print("removing not head of list ",number,node.prev_or_value)
        #if node.next != None:
          #print("next=", node.next.prev_or_value)
        prev.next = node.next
        self.add_to_free(node)
      else:#first node in the chain
        if node.next != None:
          #print("removing head of list not only",node.prev_or_value ," next=",node.next.prev_or_value)
          #copy next element to this slotand remove next node instead
          to_delete = node.next
          node.prev_or_value = node.next.prev_or_value
          node.next = node.next.next
          self.add_to_free(to_delete)
        else:
          #print("removing head of list only", node.prev_or_value)
          self.add_to_free(node)
        
  def empty(self):
    for node in self.table:
      if node.is_free != True:
        return False
    return True
    



    
    
    
  
