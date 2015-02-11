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
    
    def remove_child(self, child_rem):
        for index, child in enumerate(self.children):
            if child is child_rem:
                self.degree -= child.degree + 1
                del self.children[index]
                break
        else:
            print("\nChild with key {0} not found in node with key: {1}".format(child_rem.key, self.key))
            
    def traversal(self):
        print(self.key, end=' ->')
        for child in self.children:
            print(child.key, end=' ')
        print('\n', end=' ')
        for child in self.children:
            child.traversal()
        
    
class FibonacciHeap:
    def __init__(self):
        self.roots_list = []
        self.min_root_index = None
        
    def insert(self, elt):
        """ Simply append node to roots list, leave maintenance operations for later """
        if isinstance(elt, FibHeapNode):
            node = elt
        else:
            elt_key = elt
            node = FibHeapNode(elt)
        if self.min_root_index is None:
            self.min_root_index = 0
        else:
            min_node = self.roots_list[self.min_root_index]
            if node.key < min_node.key:
                self.min_root_index = len(self.roots_list)
        self.roots_list.append(node)
    
    def _add_as_root(self, node):
        """ Add a node as root, change its parent property, mark it as False, etc """
        node.parent = None
        node.marked = False
        self.roots_list.append(node)
    
    def extract_min(self):
        """ Removes min node, makes its children as roots and starts consolidate operation """
        if self.min_root_index is None:
            return None
        min_node = self.roots_list[self.min_root_index]
        min_key = min_node.key
        del self.roots_list[self.min_root_index]
        for children in min_node.children:
            self._add_as_root(children)
        # del(min_node) #operation not really necessary
        self._consolidate()
        self._set_min_index()
        return min_key
    
    def _consolidate(self):
        """ Merge all roots which have the same degree. (same number of children) """
        node_degree_hash = {}   #hash containing, node degree:node index pairs
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
        
    def update_key(self, old_key, new_key):
        """ 
        Search node with BFS and update key 
        IMPORTANT: only supports decrease of key, increase not supported
        """
        if old_key < new_key:
            print("New key is greater, change not possible")
            return None
        from queue import Queue
        qu = Queue()
        for root in self.roots_list:
            if root.key <= old_key:
                qu.put_nowait(root)
        while not qu.empty():
            node = qu.get_nowait()
            if node.key == old_key:
                node.key = new_key
                self._maintain_heap(node)
                break
            #accessing children of node to put into queue
            for child in node.children:
                if child.key <= old_key:
                    qu.put_nowait(child)
        else:
            #key not found, hence else is executed
            print("\nKey: {0} not found in heap, hence not updated".format(old_key))
        del(qu)
        
    def _maintain_heap(self, node):
        """ 
        Checks if node.key < parent.key if so branches it off and makes it a separate root, marking its parent (done in this method)
        If parent was already marked, the parent has to be made a separate root as well, 
        continuing until an unmarked node is found or root (done in _check_marking)
        """
        if node.parent and node.key < node.parent.key:
            father = node.parent
            father.remove_child(node)
            self.insert(node)
            self._check_marking(father)
            
    def _check_marking(self, node):
        """ If node has marked property set, remove it from its parent and make it a root, else mark it """
        if node.marked:
            self._add_as_root(node)
            if node.parent:
                self._check_marking(node.parent)
        else:
            node.marked = True
            
    
    
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
    
    