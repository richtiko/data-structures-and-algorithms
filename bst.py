class BST:
    
    def __init__(self):
        self.root = None
        
    class Node:
        
        def __init__(self):
            self.key = 0
            self.left = None
            self.right = None
            self.parent = None
            
    def insert(self, key):
        node = BST.Node()
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
        self.check_ri(self.root)
        
    def check_ri(self, node):
        if node == None:
            return
        self.less_then(node.key, node.left)
        self.bigger_then(node.key, node.right)
        self.check_ri(node.left)
        self.check_ri(node.right)
        
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
        else:
            pred = self.get_predsesor(node)
            self.delete(pred.key, pred)
            pred.left = node.left
            if node.left != None:
                node.left.parent = pred
            pred.right = node.right
            if node.right != None:
                node.right.parent = pred
            self.replace_node_for_parent(node, pred)
            
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
    
    def print_all(self):
        node = self.find_max(self.root)
        while node != None:
            print (node.key, end=',')
            node = self.get_predsesor(node)
        print("")  
        
import random

bst = BST()
bst.insert(3)
bst.insert(2)
bst.insert(2)
bst.insert(3)
bst.insert(3)
bst.insert(3)
bst.insert(2)
bst.insert(2)
bst.print_all()
bst.delete(2, bst.root)
bst.print_all()

print ("ok")

for x in range(1000):
    bst.insert( random.randint(1,1001) )

bst.check_ri(bst.root)

print ("okkkkkkkkkkkkkkk")

for x in range(1000):
    key = random.randint(1,1001)
#    bst.print_all()
#    print ("/n",key,"aaaaa")
    bst.delete(key, bst.root )
    
bst.check_ri(bst.root)
print ("ok")

