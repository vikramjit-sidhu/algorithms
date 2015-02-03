"""
Double linked list class code
"""

class LinkedList:
    """
    Class for creating a double linked list.
    """
    head = None
    tail = None

    def __iter__(self):
        self.current_node = self.__class__.head
        return self
        
        
    def __next__(self):
        if self.current_node == None:
            raise StopIteration
            
        key = self.current_node.key
        self.current_node = self.current_node.next
        return key
    
    
    def __contains__(self, key):
        for node_key in self.__iter__():
            if key == node_key:
                return True
        return False
    
        
    def add(self, key):
        """
        Given a key, makes a node and appends it to tail of linked list.
        Updates tail pointer accordingly
        """
        self.key, self.next = key, None
        
        
        if not self.__class__.head:
            #head and tail have not been set, hence setting them to self
            self.previous = None
            self.__class__.head, self.__class__.tail = self, self
            return self
        
        #tail pointer needs to be updated
        prev_tail = self.__class__.tail
        prev_tail.next = self
        self.previous = prev_tail
        self.__class__.tail = self
        
        return self.__class__.head
        
        
    def remove(self, key):
        """
        Given a key, searches for it and removes it from linked list.
        Returns the value of key
        """
        curr_node = self.__class__.head
        #cannot use self.__iter__ as the node is needed, not just key
        while curr_node:
            if curr_node.key == key:
                break
            curr_node = curr_node.next
        else:
            print("Key {0} not found, hence not deleted".format(key))
            return None
        
        #depending on curr_node position, head, tail could be updated
        prev_node = curr_node.previous
        next_node = curr_node.next
        #if there is no prev_node, curr_node is head
        if not prev_node:
            self.__class__.head = next_node
        else:
            prev_node.next = next_node
        #if there is no next_node, curr_node is tail
        if not next_node:
            self.__class__.tail = prev_node
        else:
            next_node.previous = prev_node
        
        return key

