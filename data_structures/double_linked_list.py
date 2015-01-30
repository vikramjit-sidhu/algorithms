"""
Double linked list class code
"""
import random

class LinkedList:
    """
    Class for creating a double linked list.
    """
    head = None
    tail = None
    def __init__(self, key):
        if not self.__class__.head:
            self.__class__.head = self
        self.key = key
        self.next = None
        self.previous = None
    
    
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
        if not self.__class__.tail:
            self.__class__.tail = self.__class__.head
        node = LinkedList(key)
        prev_tail = self.__class__.tail
        prev_tail.next = node
        node.previous = prev_tail
        self.__class__.tail = node
        return self.__class__.head
        
        
    def remove(self, key):
        """
        Given a key, searches for it and removes it from linked list.
        Returns the value of key
        """
        curr_node = self.__class__.head
        found = False
        while curr_node:
            if curr_node.key == key:
                found = True
                break
            curr_node = curr_node.next
        if not found:
            print("Key {0} not found, hence not deleted".format(key))
            return None
        curr_node.previous.next = curr_node.next
        curr_node.next.previous = curr_node.previous
        return key
    
        

        
def main():
    bag_num = list(range(1000))
    foo = random.choice(bag_num)
    bag_num.remove(foo)
    link_list = LinkedList(foo)

    while bag_num:
        foo = random.choice(bag_num)
        bag_num.remove(foo)
        link_list.add(foo)
        
    
    # ll = LinkedList(0)
    # for i in range(10, 210, 10):
        # ll.add(i)
        
    # for i in ll:
        # print(i)
    # ll.remove(20)
    # ll.remove(50)
    # ll.remove(670)
    # ll.remove(110)
	
    # for i in ll:
        # print(i)    
	
if __name__ == '__main__':
    main()
    