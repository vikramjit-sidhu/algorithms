"""
Priority queue implementation, using max Heap as backbone
IMPROVEMENTS: make instance variables left, right, key, value private?
"""
import sys
import fileinput

class MaxHeap:
    def __init__(self, value, key):
        self.value = value
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


    def extract_max_priority(self, root):
        """
        returns the max element in heap which as it is a max heap is root
        return value is in format (max element, new root), as since root is 
        extracted, there will be a new root
        """
        maxelt = root.key
        new_root = self.__balance_heap(root)
        return (maxelt, new_root)
        
        
    def __balance_heap(self, node):
        if not node.left or not node.right:
            return node #node is base successor
        else:
            #always choose the node which has greater key, as only it can be successor
            if node.right.key > node.left.key:
                successor = self.__balance_heap(node.right)
                #free up one of nodes childs by assigning it to successor and replacing node with successor  
                successor.parent = node.parent
                if not successor.left:
                    successor.left = node.right
                else:
                    successor.right = node.right
                node.right.parent = successor
                node.right = None
            else:
                successor = self.__balance_heap(node.left)
                successor.parent = node.parent
                if not sucessor.left:
                    successor.left = node.left
                else:
                    successor.right = node.left
                node.left.parent = successor
                node.left = None
                 
        return node
    
    
    def insert_with_priority(self, node, new_node):
    """
    
    """
        if not node.left:
            node.left = new_node
            new_node.parent = node
            return
        elif not node.right:
            node.right = new_node
            new_node.parent = node
            return
            
        if new_node.key > node.left.key:
            #insert new_node here
            new_node.left = node.left
            new_node.parent = node
            node.left.parent = new_node
            node.left = new_node
            return
        elif new_node.key > node.right.key:
            #insert new_node here
            new_node.right = node.right
            new_node.parent = node
            node.right.parent = new_node
            node.right = new_node
            return
            
        leftdiff = node.left.key - new_node.key
        rightdiff = node.right.key - new_node.key
        if leftdiff > rightdiff:
            self.insert_with_priority(node.right, new_node)
        else:
            self.insert_with_priority(node.left, new_node)
            
        
    def increment_priority(self, root, node, key, increment):
    
    
    def __reshuffle_heap(self, node):
    
    
        

def main():
    heap = generate_heap()
        
        
        
def generate_heap():
    #read list to generate heap from external file, or user input
    a = input()
    print(sys.argv[1:])
    print("input is {}".format(a))
    #for line in fileinput.input():
        #print(line)
    
    
        
        
if __name__ == '__main__':
    main()
