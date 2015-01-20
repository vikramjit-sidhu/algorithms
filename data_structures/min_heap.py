"""
Priority queue implementation, using max Heap as backbone
IMPROVEMENTS: make instance variables left, right, key, value private?
"""
from random import randint

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
            return node
        elif not node.right:
            node.right = node.left
            node.left = None
        else:
            #always choose the node which has greater key, as only it can be successor
            if node.right.key >= node.left.key:
                successor = self.__balance_heap(node.right)
                successor.left = node.left      #successor.left is the one which is always empty
            else:
                successor = self.__balance_heap(node.left)
                successor.left = node.right
            print("recursion, node.key -> {};  node.right.key -> {};  node.left.key -> {}".format(node.key, node.right.key, node.left.key))
            print("successor found -> {}".format(successor.key))        
            if successor.left:
                successor.left.parent = successor

            if not node.parent: #base case when node == root
                successor.parent = None
                return successor
            node.right = successor
            node.left = None
                 
        return node
    
    
    def insert_with_priority(self, root, new_node):
        """
        insert an element, search recursively until a position is found
        the first element lesser than new_node.key is where it is inserted
        the node which has lesser difference than new_node.key is iterated
        EDGE CASE: incase new_node will replace root

        Assuming that the root is created beforehand and is not None
        """
        if not root:
            print("UNSuccesfull in breaking the universe")

        if new_node.key > root.key:
            new_node.right = root
            root.parent = new_node
            if root.right.key > root.left.key:
                new_node.left = root.right
                root.right = None
            else:
                new_node.left = root.left
                root.left = None
            new_node.left.parent = new_node

            return new_node
        else:
            self.__insert_into_tree(root, new_node)

        return root



    def __insert_into_tree(self, node, new_node):
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
            self.__insert_into_tree(node.right, new_node)
        else:
            self.__insert_into_tree(node.left, new_node)
            
        
    def increment_priority(self, root, key_find, increment):
        """
        used to increment priority of a node key, calling method __finding_node
        after incrementing calls private method reshuffle_heap
        """
        node = self.__finding_node(root, key_find, increment)
        if not node:
            print("Key {} not found, hence not incremented in heap".format(key_find))
        else:
            new_root = self.__reshuffle_heap(node)
            if new_root:
                return new_root

        return root


    def __finding_node(self, node, key_find, increment):
        """
        find node whose priority has to be incremented
        recursive method used
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
        given node, whose key has been incremented, this method moves it up
        the heap, if needed. handles the case where node becomes the root
        """
        while node.parent and node.parent.key < node.key:
            ancestor = node.parent
            if node == ancestor.left:
                ancestor.left = node.left
                temp = ancestor.right
                ancestor.right = node.right
                node.left = ancestor
                node.right = temp
                if node.right:
                    node.right.parent = node
            else:
                ancestor.right = node.right
                temp = ancestor.left
                ancestor.left = node.left
                node.right = ancestor
                node.left = temp
                if node.left:
                    node.left.parent = node
            node.parent = ancestor.parent
            ancestor.parent = node
            if ancestor.left:
                ancestor.left.parent = ancestor
            if ancestor.right:
                ancestor.right.parent = ancestor
            
        #base case when node becomes the root (hence check in while loop for node.parent)
        if not node.parent:
            return node
        return None
    
        

def main():
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
        print(max_elt)
        
    
        
        
if __name__ == '__main__':
    main()
