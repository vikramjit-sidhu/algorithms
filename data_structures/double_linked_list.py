"""
Double linked list class code
"""
class LLNode:
    """ Node used by linked list class """
    def __init__(self, data):
        self.key = data
        self.next = None
        self.previous = None


class LinkedList:
    """ Class for creating a double linked list. It is assumed that """
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        self.current_node = self.head
        return self
        
    def __next__(self):
        if self.current_node is None:
            raise StopIteration
        key = self.current_node.key
        self.current_node = self.current_node.next
        return key
    
    def __contains__(self, key):
        for node_key in self.__iter__():
            if key is node_key:
                return True
        return False
        
    def add(self, key):
        """
        Given a key, makes a node and appends it to tail of linked list.
        Updates tail pointer accordingly
        """
        node = LLNode(key)
        if self.head is None:
            #head and tail have not been set, hence setting them to self
            self.head, self.tail = node, node
            return node
        #tail pointer needs to be updated
        prev_tail = self.tail
        prev_tail.next = node
        node.previous = prev_tail
        self.tail = node
        return self.head
        
    def remove(self, key):
        """
        Given a key, searches for it and removes it from linked list.
        Returns the value of key
        """
        curr_node = self.head
        #cannot use self.__iter__ as the node is needed, not just key
        while curr_node is not None:
            if curr_node.key is key:
                break
            curr_node = curr_node.next
        else:
            print("Key {0} not found, hence not deleted".format(key))
            return None
        #depending on curr_node position, head, tail could be updated
        prev_node = curr_node.previous
        next_node = curr_node.next
        #if there is no prev_node, curr_node is head
        if prev_node is None:
            self.head = next_node
        else:
            prev_node.next = next_node
        #if there is no next_node, curr_node is tail
        if next_node is None:
            self.tail = prev_node
        else:
            next_node.previous = prev_node
        del(curr_node)
        return key

