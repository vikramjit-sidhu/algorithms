"""
Priority queue implementation, using Binary min Heap as backbone
IMPROVEMENTS: make instance variables left, right, key, value private?
"""
from random import randint

#dangerous methods -> change structure of heap

class MaxHeap:
    def __init__(self, key, value):
        self.value = int(value)
        self.key = int(key)
        self.height = 0 #height : the number of levels below this node
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
        Moves successor(child of father) up in place of father, and 
        hence frees up one of fathers children, for it to be moved further up.
        Successor always has one child empty.
        Maintains order of children which father node had
        Returns father, ie the node which is to be moved further up tree
        
        Handles base case where father == root
        """
        if not father or not successor or (successor.left and successor.right):
            print("\n\nERROR: method __move_up_tree, null value encountered where there should not be one")
            self.__debug_print(father, successor)
            
        #need to change left, right of successor; parents of left and right
        #need to free up one of children of father
        #keep the order of the parent, with respect to position of child   
        
        if successor == father.left:
            temp = father.right
            father.right = None
            if successor.right:
                successor.left = successor.right
            successor.right = temp
        elif successor == father.right:
            temp = father.left
            father.left = None
            if successor.left:
                successor.right = successor.left
            successor.left = temp
        else:   #NOTE: due to this check, need not change successor.parent, as it is already set to father
            print("\n\nERROR: method __move_up_tree, successor is not a child of father\n")
            self.__debug_print(father, successor)
            return None

        temp.parent = successor #updating parent of temp node
        
        #updating heights
        self.__update_height(successor)
        self.__update_height(father)

        if not father.parent: #base case where node == root, return successor
            father = None
            successor.parent = None
            return successor
        return father
        
    
    def insert_node(self, root, new_node):
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
            new_root_tobalance = self.__insert_in_placeof(new_node, root)
            self.__check_node_balance(new_root_tobalance)
            return new_root_tobalance
        else:
            balance_node = self.__insert_into_tree(root, new_node)
            self.__update_height_upto(balance_node, None)
            self.__check_node_balance(balance_node)
        return root

        
    def __insert_into_tree(self, node, new_node):
        """
        Goes down heap to find appropriate position for new_node
        """
        if not node.left or not node.right:
            return self.__insert_as_child(node, new_node)
            
        if new_node.key >= node.left.key:
            return self.__insert_in_placeof(node.left, new_node)
        elif new_node.key >= node.right.key:
            return self.__insert_in_placeof(node.right, new_node)
            
        #send new_node into subtree which has lesser height
        if node.right.height <= node.left.height:
            check_balance_node = self.__insert_into_tree(node.right, new_node)
        else:
            check_balance_node = self.__insert_into_tree(node.left, new_node)

        return check_balance_node


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

        self.__update_height(father)
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
        
        Need to update child attribute (left or right) of replacing_node.parent
        Only updates height of new_node and replacing_node
        
        Returns new_node, ie the node which has been newly inserted
        """
        if not new_node or not replacing_node:
            print("\n\nERROR: method, __insert_in_placeof null values sent\n")
            return None
        
        grandfather = replacing_node.parent
        new_node.parent = grandfather #new_node parent set
        replacing_node.parent = new_node    #replacing_node parent set; new_node one child
        
        #setting child attribute of grandfather if it exists, updating it to new_node from replacing_node
        if grandfather:
            if grandfather.left == replacing_node:
                grandfather.left = new_node
            else:
                grandfather.right = new_node
        
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

        self.__update_height(replacing_node)
        self.__update_height(new_node)
        
        return new_node


    def __check_node_balance(self, node_tocheck):
        """
        Given node_tocheck, finds if height difference between subtrees of node_tocheck is <= 2.
        If this is not the case, the node needs to be rebalanced by calling method 
        The __check_node_balance method also checks balance of parent of node_tocheck recursively, upto root 
        """
        while node_tocheck:
            diff = self.height_difference_subtrees(node_tocheck)
            if diff > 2:
                self.__balance_node(node_tocheck, diff-2)
            self.__update_height(node_tocheck)
            node_tocheck = node_tocheck.parent


    #DANGEROUS METHOD
    def __balance_node(self, main_balance_node, height_needed):
        """
        Given node whose subchildren are imbalanced (height difference > 2), balances them out
        height_needed is the height of the subtree required to balance out the nodes
        A subtree of this height is extracted from the child having a larger height than the other
        """
        #find child to insert the node which is removed, ie find subtree with lesser height
        if main_balance_node.left.height < main_balance_node.right.height:
            subtree_insert_node = main_balance_node.left
        else:
            subtree_insert_node = main_balance_node.right
        
        #extract subtree of height height_needed, always from subtree with greater height
        node = main_balance_node
        while node.left or node.right:
            left = node.left.height if node.left else 0
            right = node.right.height if node.right else 0
            
            node = node.left if left >= right else node.right

        height_obtained = 1
        while height_obtained < height_needed:
            node = node.parent
            height_obtained += 1

        #remove node from its subtree
        #DANGEROUS PART
        parent_node = node.parent
        node.parent = None
        if node == parent_node.left:
            parent_node.left = None
        else:
            parent_node.right = None
            
        self.__update_height_upto(parent_node, main_balance_node)

        final_insert_position = self.__insert_subtree(subtree_insert_into, node)
        self.__update_height_upto(final_insert_position, main_balance_node)
       
        
    def __insert_subtree(self, subtree_insert_into, subtree_toinsert):
        """
        Insert subtree_toinsert into subtree subtree_insert into, insertion follows normal rule of insertion.
        Incase a node is replaced by subtree_toinsert, it will become the new subtree_toinsert and will recurse down heap
        The subtree with lesser height is chosen to insert into
        """
        current_node = subtree_insert_into
        
        while subtree_toinsert:
            if not current_node.left or not current_node.right:
                final_insertion_postition = self.__insert_as_child(current_node, subtree_to_insert)
                subtree_toinsert = None
                continue
            
            if current_node.left.key < subtree_toinsert.key:
                subtree_toinsert = self.__replace_nodes(node.left, subtree_toinsert)
            elif current_node.right.key < subtree_toinsert.key:
                subtree_toinsert = self.__replace_nodes(node.right, subtree_toinsert)

            if current_node.left.height < current_node.right.height:
                current_node = current_node.left
            else:
                current_node = current_node.right
                
        return final_insertion_postition

        
    #DANGEROUS METHOD    
    def __replace_nodes(self, node, switch_node):
        """
        Performs a replacing act, removes node from its position in heap and adds switch_node in place of it
        Need to update grandfather node (parent of node) as well
        Returns node, with parent null
        """
        if not node or not switch_node:
            print("\n\nERROR: method __switch_positions, nodes empty")
            return None
        
        grandfather = node.parent
        node.parent = None
        switch_node.parent = grandfather
        
        #setting child attribute of grandfather if it exists, updating it to new_node from replacing_node
        if grandfather:
            if grandfather.left == node:
                grandfather.left = switch_node
            else:
                grandfather.right = switch_node
            self.__update_height(grandfather)
        
        return node
    
        
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
            rval = self.__finding_node(node.left, key_find, increment)
            if not rval:
               rval = self.__finding_node(node.right, key_find, increment)
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
            self.__debug_print(father, childe)
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
        elif childe == father.right:   #additional precautionary check
            temp = father.left
            father.left = childe.left   #parent.left updated
            father.right = childe.right #parent.right updated
            childe.right = father   #childe.right updated
            childe.left = temp
            if childe.left:
                childe.left.parent = childe
        else:
            print("\n\nERROR: method, __switch_positions childe not a child node of father\n")
            self.__debug_print(father, childe)
            return None
           
        if father.left:
            father.left.parent = father
        if father.right:
            father.right.parent = father

        self.__update_height(father)
        self.__update_height(childe)

        return childe
    

    def __update_height(self, node):
        """
        Given node, updates height attribute, by taking max of
        the height of its 2 children (if they exist)
        """
        if not node:
            print("\n\nERROR: method __update_height method, node is null\n")
            return None

        ht_left = node.left.height if node.left else 0
        ht_right = node.right.height if node.right else 0

        node.height = max(ht_left, ht_right) + 1


    def __update_height_upto(self, update_height_node, limit_node):
        """
        Updates height of nodes upto limit_node
        Does NOT update height of limit_node
        """
        if not update_height_node:
            print("\n\nERROR: method __update_height_upto, update_height_node is null\n")
            return None
        while update_height_node != limit_node:
            self.__update_height(update_height_node)
            update_height_node = update_height_node.parent



    def height_difference_subtrees(self, node):
        """
        Returns the height difference between the 2 children of node
        """
        if not node:
            print("\n\nERROR: method __update_height, method node is null\n")
            return None

        ht_left = node.left.height if node.left else 0
        ht_right = node.right.height if node.right else 0

        return int(abs(ht_left-ht_right))

        
    def __debug_print(self, parent, child):
        """
        Function used for debugging, prints parent and child (if present),
        along with their child values
        """
        if parent:
            print("parent present; key -> {}".format(parent.key))
            if parent.right:
                print("parent right child -> {}".format(parent.right.key))
            else:
                print("parent right child null")
            if parent.left:
                print("parent left child -> {}".format(parent.left.key))
            else:
                print("parent left child null")   
        else:
            print("parent node null")
            
        if child:
            print("child present; key -> {}".format(child.key))
            if child.right:
                print("child right child -> {}".format(child.right.key))
            else:
                print("child right child null")
            if child.left:
                print("child left child -> {}".format(child.left.key))
            else:
                print("child left child null")   
        else:
            print("child node null")


    def inorder_traversal(self, node):
        if not node:
            return "null"
        par = node.parent.key if node.parent else "null"
        print("{} <-- {} parent-{}, height-{} --> {}".format(self.inorder_traversal(node.left), node.key, par, node.height, self.inorder_traversal(node.right)))
        return node.key
        
        

def main():
    heap = generate_heap()
        
        
        
def generate_heap():
    #read list to generate heap from external file
    node_value = 1
    root = MaxHeap(randint(0, 130), node_value)
    print("\nInorder Traversal")
    root.inorder_traversal(root)
    print("\n")

    for i in range(0, 130, 7):
        node_value += 1
        new_node = MaxHeap(i, node_value)
        print("Inserting node no {} with key -> {} into heap".format(new_node.value, new_node.key))
        root = root.insert_node(root, new_node)
        print("\nInorder Traversal")
        root.inorder_traversal(root)
        print("\n")

    
        
    # for i in range(0, 130, 7):
        # root = root.increment_priority(root, i, randint(0, 130))
        

    # while root:
        # max_elt, root = root.extract_max_priority(root)
        # print("\n{}".format(max_elt))
        
    
        
        
if __name__ == '__main__':
    main()
