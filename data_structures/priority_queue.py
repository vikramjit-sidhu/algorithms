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
        #handling base case here
        if not root.right:
            root.left.parent = root.parent
            new_root = root.left
        elif not root.left:
            root.right.parent = root.parent
            new_root = root.right
        else:
            new_root = self.__balance_heap(root)

        return (maxelt, new_root)
        
        
    def __balance_heap(self, node):
        """
        after the method extract_max_priority is called, the heap needs to
        be reshuffled to find a new root
        """
        if not node.left:
            #nothing to do here
        elif not node.right:
            node.right = node.left
            node.left = None
        else:
            #always choose the node which has greater key, as only it can be successor
            #ADD A CHECK TO SEE IF NODE.PARENT = NONE, ONLY THEN CHANGE PARENT OF SUCCESSOR
            if node.right.key > node.left.key:
                successor = self.__balance_heap(node.right)
                successor.left = node.left
                node.left.parent = successor
            else:
                successor = self.__balance_heap(node.left)
                successor.left = node.right
                node.right.parent = successor

            if not node.parent: #base case when node == root
                successor.parent = None
                return successor
            node.right = sucessor
            node.left = None
                 
        return node
    
    
    def insert_with_priority(self, node, new_node):
        """
        insert an element, search recursively until a position is found
        the first element lesser than new_node.key is where it is inserted
        the node which has lesser difference than new_node.key is iterated
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
            
        
    def increment_priority(self, node, key_find, value_find, increment):    #argument node shoulde be = root
        """
        used to increment priority of a node key
        after incrementing calls private method reshuffle_heap
        """
        while node.key != key_find:
            if node.left.key < key_find:
                node = node.right
                continue
            elif node.right.key < key.find:
                node = node.left
                continue

            ldiff = node.left.key - key_find
            rdiff = node.right.key - key_find
            if ldiff < rdiff:
                node = node.right
                continue
            node = node.left    #as rdiff < ldiff

        node.key += increment
        self.__reshuffle_heap(node)
    
    
    def __reshuffle_heap(self, node):
        while node.parent.key < node.key:
            ancestor = node.parent
            if node == ancestor.left:
                ancestor.left = node.left
                temp = ancestor.right
                ancestor.right = node.right
                node.right = temp
                node.left = ancestor
            else:
                ancestor.right = node.right
                temp = ancestor.left
                ancestor.left = node.left
                node.left = temp
                node.right = ancestor
            node.parent = ancestor.parent
            ancestor.parent = node
    
        

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
