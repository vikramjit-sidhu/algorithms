"""
Fibonacci heap implementation
http://www.growingwiththeweb.com/2014/06/fibonacci-heap.html
http://stackoverflow.com/questions/19508526/what-is-the-intuition-behind-the-fibonacci-heap-data-structure
http://stackoverflow.com/questions/14333314/why-is-a-fibonacci-heap-called-a-fibonacci-heap
"""

class FibHeapNode:
    def __init__(self, key):
        self.key = key
        self.children = []
        self.parent = None
        self.degree = 0 #no of children
        self.marked = False #has a child node been removed
    
    def _update_degree(self):
        self.degree = 0
        for child in self.children:
            self.degree += child.degree + 1
    
    def insert_child(self, node):
        """ Inserts a child node into the object from where method is called """
        node.parent = self
        self.children.append(node)
        self.degree += node.degree + 1
        
    
class FibonacciHeap:
    def __init__(self):
        self.roots_list = []
        self.min_root_index = None
        
    def insert(self, key):
        node = FibHeapNode(key)
        if self.min_root_index is None:
            self.min_root_index = 0
        else:
            min_node = self.roots_list[self.min_root_index]
            if key < min_node.key:
                self.min_root_index = len(self.roots_list)
        self.roots_list.append(node)
        
    def extract_min(self):
        if self.min_root_index is None:
            return None
        min_node = self.roots_list[self.min_root_index]
        min_key = min_node.key
        del self.roots_list[self.min_root_index]
        for children in min_node.children:
            self.roots_list.append(children)
        del(min_node)
        self._consolidate()
        self._set_min_index()
        return min_key
    
    def _consolidate(self):
        """ Merge all roots which have the same degree. """
        node_degree_hash = {}   #hash containing node degree:node index pairs
        for node in self.roots_list:
            if node.degree in node_degree_hash:
                while node.degree in node_degree_hash:
                    #other node, with same degree, which has to be merged
                    merge_node = node_degree_hash[node.degree]
                    #deleting this degree entry from node_degree_hash as we are merging them
                    del node_degree_hash[node.degree]
                    node = self._merge(node, merge_node)
            node_degree_hash[node.degree] = node
        #update roots_list with new roots
        self.roots_list = list(node_degree_hash.values())

    def _merge(self, node1, node2):
        """ node with smaller key becomes a child of other node """
        if node1.key < node2.key:
            node1.insert_child(node2)
            return node1
        node2.insert_child(node1)
        return node2
    
    def _set_min_index(self):
        """ Iterates through all roots of heap and sets pointer to one with minimum key """
        min_val = self.roots_list[0].key if self.roots_list else 0
        min_index = None
        for index, node in enumerate(self.roots_list):
            if node.key < min_val:
                min_val = node.key
                min_index = index
        self.min_root_index = min_index
        
    def update_key(self, new_key):
        
    

def heap_node_test():
    node_main = FibHeapNode(8)
    for i in range(10):
        node = FibHeapNode(i*10)
        node_main.insert_child(node)
    print("degree: {0}".format(node_main.degree))
    for node in node_main.children:
        print(node.key)
        
def fib_heap_test():
    hp = FibonacciHeap()
    for i in range(20):
        hp.insert(i)
    print("\n\nmin root index: {0} min root key(should be 0): {1}".format(hp.min_root_index, hp.roots_list[hp.min_root_index].key))
    min_node = hp.roots_list[hp.min_root_index]
    for i in range(-2, 10, 3):
        min_node.insert_child(FibHeapNode(i))
    print("extracted min node: {0}".format(hp.extract_min()))
    print("min root index: {0} min root key(should be -2): {1}".format(hp.min_root_index, hp.roots_list[hp.min_root_index].key))
    
def main():
    heap_node_test()
    fib_heap_test()
        
if __name__ == '__main__':
    main()
    
    