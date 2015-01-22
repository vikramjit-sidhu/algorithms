"""
Priority queue implementation, using max Heap as backbone
IMPROVEMENTS: make instance variables left, right, key, value private?
"""
from random import randint

#dangerous methods -> change structure of heap

class MaxHeap:
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


    def extract_max_priority(self, root):
        """
        returns the max priority element in heap which as it is a max heap is root
        return value is in format (max element, new root), since root is 
        extracted, there will be a new root
        """
        maxelt = root.key
        #handling base case here
        if not root.left and not root.right:
            new_root = None     #no more elements left in heap
        elif not root.right:
            new_root = self.__move_up_tree(root, root.left)
        elif not root.left:
            new_root = self.__move_up_tree(root, root.right)
        else:
            new_root = self.__balance_heap(root)

        return (maxelt, new_root)
        
        
    def __balance_heap(self, node):
        """
        finds a successor for node(among its children), going down heap till one is found
        successor is defined as having one of its children empty (None)
        """
        if node.right and node.left:
            #always choose the node which has greater key, as only it can be successor
            if node.right.key >= node.left.key:
                successor = self.__balance_heap(node.right)
            else:
                successor = self.__balance_heap(node.left)
            node = self.__move_up_tree(node, successor)

        return node
    
    
#DANGEROUS METHOD    
    def __move_up_tree(self, father, successor):
        """
        moves successor(child of node) up in place of node, and 
        hence frees up one of nodes children, for it to be moved further up
        successor always has one child empty
        returns node, ie the one which is to be moved up tree further
        
        should handle base case where node == root
        """
        if not father or not successor or not (successor.left and successor.right):
            print("\n\nERROR: method __move_up_tree, null value encountered where there should not be one\n")
            return None
        #need to change left, right of successor; parents of left and right
        #need to free up one of children of father
        #keep the order of the parent, with respect to position of child   
        
        if successor == father.left:
            temp = father.right
            father.right = None
        elif successor == father.right:
            temp = father.left
            father.left = None
        else:   #NOTE: due to this check, need not change successor.parent, as it is already set to father
            print("\n\nERROR: method __move_up_tree, successor is not a child of father\n")
            return None

        temp.parent = successor #updating parent of temp node
        
        #finding out which of child nodes, successor has free, assigning it to other child of father
        if not successor.left:
            successor.left = temp
        else:
            successor.right = temp
        
        if not father.parent: #base case where node == root, return successor
            father = None
            successor.parent = None
            return successor
        return father
        
    
    def insert_with_priority(self, root, new_node):
        """
        insert an element, search recursively until a position is found
        the first element lesser than new_node.key is where it is inserted
        the node which has lesser difference than new_node.key is iterated
        EDGE CASE: incase new_node will replace root
        """
        if not root or not new_node:
            print("\n\nERROR: method, insert_with_priority, one of nodes is null\n")
            return None

        if new_node.key > root.key:
            return self.__insert_in_placeof(new_node, root)
        else:
            self.__insert_into_tree(root, new_node)
        return root

        
    def __insert_into_tree(self, node, new_node):
        """
        Goes down heap to find appropriate position for new_node
        """
        if not node.left or not node.right:
            self.__insert_as_child(node, new_node)
            return
            
        if new_node.key > node.left.key:
            self.__insert_in_placeof(new_node, node.left)
            return
        elif new_node.key > node.right.key:
            self.__insert_in_placeof(new_node, node.right)
            return
            
        #send new_node into subtree where it has lesser difference    
        leftdiff = node.left.key - new_node.key
        rightdiff = node.right.key - new_node.key
        if leftdiff > rightdiff:
            self.__insert_into_tree(node.right, new_node)
        else:
            self.__insert_into_tree(node.left, new_node)


#DANGEROUS METHOD            
    def __insert_as_child(self, father, child):
        """
        Inserts child as a well, child of father node.
        father node has one of its children free, so no modifications required
        """
        if not father or not child:
            print("\n\nERROR: method __insert_as_child one of nodes is empty\n")
            
        if not father.left:
            father.left = child
            child.parent = father
        elif not father.right:
            father.right = child
            child.parent = father
        else:
            print("\n\nERROR: method __insert_as_child father node does not have empty child\n")
        return father
            

#DANGEROUS METHOD     
    def __insert_in_placeof(self, new_node, replacing_node):
        """
        Substitutes new_node in place of replacing_node.
        new_node only has its key and value set, its right, left and parent are None.
        replacing_node becomes a child of new_node and has one of its children move up and become a
        child of new_node.
        Keeps order of child moving up in new_node, ie if left child of replacing_node moves up, 
        it will be left child in new_node.
        
        Returns new_node, ie the node which has been newly inserted
        """
        if not new_node or not replacing_node:
            print("\n\nERROR: method, __insert_in_placeof null values sent\n")
            return None
            
        new_node.parent = replacing_node.parent #new_node parent set
        replacing_node.parent = new_node    #replacing_node parent set; new_node one child
        
        #setting new_node children
        if replacing_node.right:
            if replacing_node.left:
                if replacing_node.left.key > replacing_node.right.key:
                    new_node.left = replacing_node.left
                    new_node.left.parent = new_node
                    new_node.right = replacing_node
                    replacing_node.left = None
                    return new_node
            new_node.right = replacing_node.right
            new_node.right.parent = new_node
            new_node.left = replacing_node
            replacing_node.right = None
        else:
            new_node.left = replacing_node.left
            if new_node.left:
                new_node.left.parent = new_node
                replacing_node.left = None
            new_node.right = replacing_node
            
        return new_node
        
        
    def increment_priority(self, root, key_find, increment):
        """
        used to increment priority of a node key, calling method __finding_node
        after incrementing calls private method reshuffle_heap
        """
        node = self.__finding_node(root, key_find, increment)
        if not node:
            print("\n\nWhile incrementing priority, key {} not found, hence not incremented in heap\n".format(key_find))
        else:
            new_root = self.__reshuffle_heap(node)
            if new_root:
                return new_root

        return root


    def __finding_node(self, node, key_find, increment):
        """
        Find node whose priority has to be incremented by going down tree
        """
        if node.key == key_find:
            node.key += increment
            return node
        elif node.left and node.right and node.left.key > key_find and node.right.key > key_find:
            ldiff = node.left.key - key_find
            rdiff = node.right.key - key_find
            if ldiff < rdiff:
                rval = self.__finding_node(node.left, key_find, increment)
                if not rval:
                    rval = self.__finding_node(node.right, key_find, increment)
            else:
                rval = self.__finding_node(node.right, key_find, increment)
                if not rval:
                    rval = self.__finding_node(node.left, key_find, increment)
            return rval
        elif node.left and node.left.key >= key_find:
            return self.__finding_node(node.left, key_find, increment)
        elif node.right and node.right.key >= key_find:
            return self.__finding_node(node.right, key_find, increment)
            
        return None
    
    
    def __reshuffle_heap(self, node):
        """
        Given node, whose key has been incremented, this method calls __switch_positions method to move
        node up the heap, if needed. 
        Returns node only if it becomes the root, else returns None
        """
        while node.parent and node.parent.key < node.key:
            node = self.__switch_positions(node.parent, node)
        #base case when node becomes the root (hence check in while loop for node.parent)
        if not node.parent:
            return node
        return None
    

#DANGEROUS METHOD     
    def __switch_positions(self, father, childe):
        """
        Given a parent and its child, switch their positions exactly,without altering the position of the child nodes.
        Returns the childe node, ie the new parent
        """
        if not father or not childe:
            print("\n\nERROR: method, __switch_positions null nodes sent\n")
            return None
            
        childe.parent = father.parent   #childe.parent updated
        father.parent = childe  #father.parent updated
        if childe == father.left:
            temp = father.right
            father.left = childe.left   #parent.left updated
            father.right = childe.right #parent.right updated
            childe.left = father    #childe.left updated
            childe.right = temp #childe.right updated
            if childe.right:
                childe.right.parent = childe    #childe.right child parent updated
        else:   #childe == father.right
            temp = father.left
            father.left = childe.left   #parent.left updated
            father.right = childe.right #parent.right updated
            childe.right = father   #childe.left updated
            childe.left = temp
            if childe.left:
                childe.left.parent = childe
           
        if father.left:
            father.left.parent = father
        if father.right:
            father.right.parent = father
            
        return childe
            
    

def main():
    sys.stdout = open("output.txt", "w")
    heap = generate_heap()
        
        
        
def generate_heap():
    #read list to generate heap from external file
    node_value = 1
    root = MaxHeap(randint(0, 130), node_value)

    for i in range(0, 130, 7):
        node_value += 1
        new_node = MaxHeap(i, node_value)
        root = root.insert_with_priority(root, new_node)
        
    # for i in range(0, 130, 7):
        # print("calling method root.key -> {}, key_find -> {}".format(root.key, i))
        # root = root.increment_priority(root, i, randint(0, 130))
    root = root.increment_priority(root, 0, randint(0, 130))

    while root:
        max_elt, root = root.extract_max_priority(root)
        print("\n{}".format(max_elt))
        
    
        
        
if __name__ == '__main__':
    main()
