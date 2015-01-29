"""
Double linked list class code
"""
import random

class LinkedList:
    """
    Class for creating a double linked list.
    """
    _head = None
    _tail = None
    def __init__(self, key):
        if not self._head:
            self._head = self
        self.key = key
        self.next = None
        self.previous = None
    
    
    def __iter__(self):
        self.current_node = self._head
        return self
        
        
    def __next__(self):
        if self.current_node == None:
            raise StopIteration
            
        key = self.current_node.key
        self.current_node = self.current_node.next
        return key
    
    
    def __contains__(self, key):
        for node in self.__iter__():
            print(node)
    
    # def set_head(self, node):
        # """
        # Set root of linked list
        # """
        # self._head = node
        # return self._head
        
        
    def add_node(self, node):
        """
        Adds a node to end of linked list, updates the tail pointer
        """
        if not self._tail:
            self._tail = self._head
        self._tail.next = node
        node.previous = self._tail
        self._tail = node
        return self._head
        

        
def main():
    bag_num = list(range(500))
    foo = random.choice(bag_num)
    bag_num.remove(foo)
    
    root = LinkedList(foo)
    root.set_head(root)
    
	
	
if __name__ == '__main__':
    main()