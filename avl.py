class AVL:
    
    def __init__(self):
        self.root = None
        
    class Node:
        
        def __init__(self):
            self.key = 0
            self.left = None
            self.right = None
            self.parent = None
            self.height = 0
            
    def insert(self, key):
        node = AVL.Node()
        node.key = key 
        parent = None
        n = self.root
        while n != None :
            parent = n
            if n.key >= node.key :
                n = n.left
            else:
                n = n.right
        if parent == None :
            self.root = node
        elif parent.key >= node.key :
            parent.left = node
        else:
            parent.right = node
        node.parent = parent
        self.update_heights_to_up(parent)
        self.check_ri(self.root)

    def update_heights_to_up(self, node):
        while node != None:
            node = self.update_height_and_stabilize(node)
            node = node.parent
            
    def update_height_and_stabilize(self, node):
        if self.check_child_heights(node) == False :
            self.fix_child_heights(node)
        node.height = max(self.height(node.left) , self.height(node.right)) + 1
        return node

    def check_child_heights(self, node):
        return abs(self.height(node.right) - self.height(node.left)) <= 1

    def fix_child_heights(self , node):
        if self.height(node.right) > self.height(node.left):
            if self.height(node.right.right) >= self.height(node.right.left):
                self.left_rotate(node)
            else:
                self.right_rotate(node.right) #make highest nodes all right
                self.left_rotate(node)
        else:
            if self.height(node.left.left) >= self.height(node.left.right):
                self.right_rotate(node)
            else:
                self.left_rotate(node.left) #make highest nodes all left
                self.right_rotate(node)

    def height (self, node):
        if node == None:
            return -1
        return node.height
        
    def left_rotate(self, node):
        x = node
        y = node.right
        #B
        x.right = y.left
        if x.right != None:
            x.right.parent = x
        #Y
        if x.parent != None:
            if x.parent.left == x:
                x.parent.left = y
            else:
                x.parent.right = y
        y.parent = x.parent
        if y.parent == None:
            self.root = y
        #X
        y.left = x
        x.parent = y
        self.update_height_and_stabilize(x)
        self.update_height_and_stabilize(y)

    def right_rotate(self, node):
        y = node
        x = node.left
        #B
        y.left = x.right
        if y.left != None:
            y.left.parent = y
        #X
        if y.parent != None:
            if y.parent.left == y:
                y.parent.left = x
            else:
                y.parent.right = x
        x.parent = y.parent
        if x.parent == None:
            self.root = x
        #Y
        x.right = y
        y.parent = x
        self.update_height_and_stabilize(y)
        self.update_height_and_stabilize(x)

    

    def replace_node_for_parent(self, node, replacement):
        if node.parent == None:
            self.root = replacement
        elif node == node.parent.left:
            node.parent.left = replacement
        else:
            node.parent.right = replacement
        if replacement != None:
            replacement.parent = node.parent

   
        
    def delete(self, key, root):
        node = self.find(key, root)
        if node == None:
            return
        
        if node.right == None or node.left == None:
            child = node.right
            if node.right == None:
                child = node.left
            self.replace_node_for_parent(node, child)
            self.update_heights_to_up(node.parent)
              
        else:
            pred = self.get_predsesor(node)
            self.delete(pred.key, pred)# this call will fix heights
            pred.left = node.left
            if node.left != None:
                node.left.parent = pred
            pred.right = node.right
            if node.right != None:
                node.right.parent = pred
            self.replace_node_for_parent(node, pred)
            pred.height = node.height
            #we dont need to chach heights in this cse because node was replaced and not removed

        parent = node.parent
        del node
        

        self.check_ri(self.root)
        
    def find(self, key, root):
        n = root
        while n != None :
            if key == n.key :
                return n
            elif n.key > key :
                n = n.left
            else:
                n = n.right
        return n

    def get_predsesor(self, node):
        if node.left == None:
            while node.parent != None and node.parent.left == node:
                node = node.parent
            return node.parent
        else:
            return self.find_max(node.left)
            
    def find_max(self, node):
        if node == None:
            return None
        while node.right != None:
            node = node.right
        return node


    def check_ri(self, node):
        if node == None:
            return
        self.less_then(node.key, node.left)
        self.bigger_then(node.key, node.right)
        if abs(self.get_height_deep(node.right) - self.get_height_deep(node.left)) >= 2 :
            raise RuntimeError("depths dont match")
        if (node.left != None and node.left.parent != node) or (node.right != None and node.right.parent != node):
            raise RuntimeError("parent error")
        self.check_ri(node.left)
        self.check_ri(node.right)
        
    def get_height_deep(self, node):
        if node == None:
            return -1
        left_height = self.get_height_deep(node.left)
        right_height = self.get_height_deep(node.right)
        if abs(left_height - right_height ) >= 2 :
            raise RuntimeError("depths dont match")
        return max(left_height,right_height)+1

    def less_then(self, key, node):
        if node == None:
            return
        if node.key > key:
            raise "error"
        self.less_then(key, node.left)
        self.less_then(key, node.right)
        
    def bigger_then(self, key, node):
        if node == None:
            return
        if node.key <= key:
            raise "error"
        self.bigger_then(key, node.left)
        self.bigger_then(key, node.right)

    
    def print_all(self):
        node = self.find_max(self.root)
        while node != None:
            print (node.key, end=',')
            node = self.get_predsesor(node)
        print("")
    
    def print_tree(self):
        nodes = []
        nodes.append(self.root)
        count = 0
        power = 0
        non_none = 0

        if self.root != None:
            non_none += 1
        while len(nodes) > 0 and non_none > 0:
            count += 1
            node = nodes.pop(0)
            if node != None:
                non_none -= 1
                print(node.key, end=' ')
                
                nodes.append(node.left)
                if node.left != None:
                    non_none += 1
                
                nodes.append(node.right)
                if node.right != None:
                    non_none += 1
            else:
                print('*', end=' ')
                nodes.append(None)
                nodes.append(None)
            if count == 2**power:
                print(" ")
                count=0
                power += 1
        print("")
        
import random
import sys

avl = AVL()
##avl.insert(3)
##avl.insert(2)
##avl.insert(6)
##avl.insert(5)
##avl.insert(10)
##avl.insert(11)
##avl.insert(12)
##avl.insert(7)
##avl.print_tree()
##avl.delete(2, avl.root)
##avl.print_all()

print ("ok")

numbers = []
for x in range(500):
    key = random.randint(1,10000)
    if avl.find(key, avl.root) == None :
        avl.insert( key )
        numbers.append(key)


print ("okaaaa", len(numbers))
##
count = 0
for x in range(500):
    if len(numbers) == 0:
        break
    if len(numbers) == 1:
        key = 0
    else:
        key = random.randint(0,len(numbers)-1)
    #if bst.find(numbers[key], bst.root) != bst.nil :
        #print("\n############################# ", key)
        #bst.print_tree()
    avl.delete( numbers[key], avl.root)
    numbers.pop(key)
    count +=1

print ("okaaaa", len(numbers))


