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
            #self.print_tree()
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
        #if replacement != self.nil:
        replacement.parent = node.parent

    def delete(self, key):
        node = self.find(key, self.root)
        if node == self.nil:
            return
        y = node
        y_color = y.color
        if y.right == self.nil or y.left == self.nil:
            x = y.right
            if y.right == self.nil:
                x = y.left
            self.replace_node_for_parent(y, x)
            
        else:
            y = self.find_min(node.right)
            y_color = y.color
            x = y.right
            x.parent = y # in case of x == nil we will nned to have parent of x pointing to y
            
            if y == node.right:
                y.left = node.left
                y.left.parent = y
                self.replace_node_for_parent(node, y)
            else:
                self.replace_node_for_parent(y, x)
                self.replace_node_for_parent(node, y)
                y.right = node.right
                y.right.parent = y
                y.left = node.left
                y.left.parent = y
            y.color = node.color    
            
        del node
        if y_color == Color.Black:
            #self.print_tree();
            self.RB_delete_fixup(x)
        self.check_ri(self.root)

    def RB_delete_fixup(self, x):
        while x != self.root and x.color == Color.Black:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == Color.Red:
                    x.parent.color = Color.Red
                    w.color = Color.Black
                    self.left_rotate(x.parent)
                    w = x.parent.right
                
                if w.left.color == Color.Black and w.right.color == Color.Black:
                    w.color = Color.Red
                    x = x.parent
                else:
                    if w.right.color == Color.Black:
                        w.left.color = Color.Black
                        w.color = Color.Red
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = w.parent.color
                    w.parent.color = Color.Black
                    w.right.color = Color.Black
                    self.left_rotate(w.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == Color.Red:
                    x.parent.color = Color.Red
                    w.color = Color.Black
                    self.right_rotate(x.parent)
                    w = x.parent.left
                
                if w.left.color == Color.Black and w.right.color == Color.Black:
                    w.color = Color.Red
                    x = x.parent
                else:
                    if w.left.color == Color.Black:
                        w.right.color = Color.Black
                        w.color = Color.Red
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = w.parent.color
                    w.parent.color = Color.Black
                    w.left.color = Color.Black
                    self.right_rotate(w.parent)
                    x = self.root
                    
        self.nil.left = self.nil.right = self.nil.parent = None
        x.color = Color.Black 
            
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

    def find_min(self, node):
        if node == self.nil:
            return self.nil
        while node.left != self.nil:
            node = node.left
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
##
##bst.insert(3846)
##bst.insert(1090)
##bst.insert(4679)
####
##bst.root.left.color = Color.Black
##bst.root.right.color = Color.Black
##bst.print_tree()
##bst.delete(1090)
##
##
####bst.insert(5)
####bst.insert(70)
##bst.print_tree()
##bst.insert(29)


#sys.exit(0)

print ("ok")
numbers = []
for x in range(1000):
    key = random.randint(1,10000)
    if bst.find(key, bst.root) == bst.nil :
        bst.insert( key )
        numbers.append(key)
        #bst.print_tree()


print ("okaaaa", len(numbers))

count = 0
for x in range(10000):
    if len(numbers) == 0:
        break
    if len(numbers) == 1:
        key = 0
    else:
        key = random.randint(0,len(numbers)-1)
    #if bst.find(numbers[key], bst.root) != bst.nil :
        #print("\n############################# ", key)
        #bst.print_tree()
    bst.delete( numbers[key] )
    numbers.pop(key)
    count +=1
    
        
print ("ok ",count)

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

