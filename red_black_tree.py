from enum import Enum

class Color(Enum):
    Black=1
    Red=2
    
    
class Node:    
    def __init__(self):
        self.key = 0
        self.left = None
        self.right = None
        self.parent = None
        self.color = Color.Black


class RedBlackTree:
        
    def __init__(self):
        self.nil = Node()
        self.nil.color = Color.Black
        self.root = self.nil
            
    def insert(self, key):
        node = Node()
        node.parent = self.nil
        node.left = self.nil
        node.right = self.nil
        node.key = key
        node.color = Color.Red
        parent = self.nil
        n = self.root
        while n != self.nil :
            parent = n
            if n.key >= node.key :
                n = n.left
            else:
                n = n.right
        if parent == self.nil :
            self.root = node
        elif parent.key >= node.key :
            parent.left = node
        else:
            parent.right = node
        node.parent = parent
        if key == 29:
            self.print_tree()
        
        self.insert_fixup(node)
        self.check_ri(self.root)

    def insert_fixup(self, node):
        while(node.parent.color == Color.Red):
            grand_parent = node.parent.parent
            parent = node.parent
            if parent == grand_parent.left:
                uncle = grand_parent.right
                if uncle.color == Color.Red:
                    parent.color = Color.Black
                    uncle.color = Color.Black
                    grand_parent.color = Color.Red
                    node = grand_parent
                else:
                    if node == parent.right:
                        node = parent
                        self.left_rotate(parent)
                    self.right_rotate(grand_parent)
                    node.parent.color = Color.Black
                    grand_parent.color = Color.Red
            else:
                uncle = grand_parent.left
                if uncle.color == Color.Red:
                    parent.color = Color.Black
                    uncle.color = Color.Black
                    grand_parent.color = Color.Red
                    node = grand_parent
                else:
                    if node == parent.left:
                        node = parent
                        self.right_rotate(parent)
                    self.left_rotate(grand_parent)
                    node.parent.color = Color.Black
                    grand_parent.color = Color.Red
        self.root.color = Color.Black
        
    def check_ri(self, node):
        if self.root.color != Color.Black:
            raise RuntimeError("root color is not black")
        
        if self.nil.color != Color.Black:
            raise RuntimeError("nil color is not black")
        
        if node == self.nil:
            return 0
        self.less_then(node.key, node.left)
        self.bigger_then(node.key, node.right)
        left_black_height = self.check_ri(node.left)
        right_black_height = self.check_ri(node.right)
        if node.color == Color.Red and (node.left.color == Color.Red or node.right.color == Color.Red):
            self.print_tree()
            raise RuntimeError("red parent has red children")
        if node.left.color == Color.Black:
           left_black_height +=1
        if node.right.color == Color.Black:
           right_black_height +=1
        if right_black_height != left_black_height:
            self.print_tree()
            raise RuntimeError("left and right black heights dont match")
        
        return right_black_height
        
    def less_then(self, key, node):
        if node == self.nil:
            return
        if node.key > key:
            raise RuntimeError("error")
        self.less_then(key, node.left)
        self.less_then(key, node.right)
        
    def bigger_then(self, key, node):
        if node == self.nil:
            return
        if node.key <= key:
            raise RuntimeError("error")
        self.bigger_then(key, node.left)
        self.bigger_then(key, node.right)

    def replace_node_for_parent(self, node, replacement):
        if node.parent == self.nil:
            self.root = replacement
        elif node == node.parent.left:
            node.parent.left = replacement
        else:
            node.parent.right = replacement
        if replacement != self.nil:
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
        while n != self.nil :
            if key == n.key :
                return n
            elif n.key > key :
                n = n.left
            else:
                n = n.right
        return n

    def left_rotate(self, node):
        x = node
        y = node.right
        #B
        x.right = y.left
        if x.right != self.nil:
            x.right.parent = x
        #Y
        if x.parent != self.nil:
            if x.parent.left == x:
                x.parent.left = y
            else:
                x.parent.right = y
        y.parent = x.parent
        if y.parent == self.nil:
            self.root = y
        #X
        y.left = x
        x.parent = y

    def right_rotate(self, node):
        y = node
        x = node.left
        #B
        y.left = x.right
        if y.left != self.nil:
            y.left.parent = y
        #X
        if y.parent != self.nil:
            if y.parent.left == y:
                y.parent.left = x
            else:
                y.parent.right = x
        x.parent = y.parent
        if x.parent == self.nil:
            self.root = x
        #Y
        x.right = y
        y.parent = x
        
    def get_predsesor(self, node):
        if node.left == self.nil:
            while node.parent != self.nil and node.parent.left == node:
                node = node.parent
            return node.parent
        else:
            return self.find_max(node.left)
            
    def find_max(self, node):
        if node == self.nil:
            return self.nil
        while node.right != self.nil:
            node = node.right
        return node
    
    def print_all(self):
        node = self.find_max(self.root)
        while node != self.nil:
            print (node.key, end=',')
            node = self.get_predsesor(node)
        print("")  

    def print_tree(self):
        nodes = []
        nodes.append(self.root)
        count = 0
        power = 0
        non_none = 0

        if self.root != self.nil:
            non_none += 1
        while len(nodes) > 0 and non_none > 0:
            count += 1
            node = nodes.pop(0)
            if node != self.nil:
                non_none -= 1
                print(node.key, node.color, end=' ')
                
                nodes.append(node.left)
                if node.left != self.nil:
                    non_none += 1
                
                nodes.append(node.right)
                if node.right != self.nil:
                    non_none += 1
            else:
                print('*', end=' ')
                nodes.append(self.nil)
                nodes.append(self.nil)
            if count == 2**power:
                print(" ")
                count=0
                power += 1
        print("----")
        
import random
import sys

bst = RedBlackTree()
bst.insert(3)
bst.insert(2)
bst.insert(81)
bst.insert(5)
bst.insert(70)
bst.print_tree()
bst.insert(29)


#sys.exit(0)

print ("ok")

for x in range(1000):
    key = random.randint(1,10000)
    if bst.find(key, bst.root) == bst.nil :
        bst.insert( key )
        #bst.print_tree()

print ("ok")

##bst.check_ri(bst.root)
##
##print ("okkkkkkkkkkkkkkk")
##
##for x in range(1000):
##    key = random.randint(1,1001)
###    bst.print_all()
###    print ("/n",key,"aaaaa")
##    bst.delete(key, bst.root )
##    
##bst.check_ri(bst.root)
##print ("ok")

