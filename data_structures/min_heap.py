"""
Creates a max heap, can also use heap sort algorithm on a pre created array
Uses an array to implement array
My implementation of python heapq module
"""

class MinHeap:
    def __init__(self, ar=[None]):
        self.A = ar
        if len(self.A) > 1:
            self.__create_minheap()


    def __min_heapify(self, index):
        left, right = 2*index, 2*index+1
        if left < len(self.A) and self.A[index] > self.A[left]:
            minimum = left
        else:
            minimum = index
        if right < len(self.A) and self.A[minimum] > self.A[right]:
            minimum = right
            
        if minimum != index:
            self.A[index], self.A[minimum] = self.A[minimum], self.A[index]
            self.__min_heapify(minimum)
            return True
        return False
        

    def __create_minheap(self):
        if self.A[0]:
            self.A.append(self.A[0])
            self.A[0] = None
        start_index = int((len(self.A)-1)/2)
        for i in range(start_index, 0, -1):
            self.__min_heapify(i)
    

    def find_min(self):
        return self.A[1]
    

    def extract_min(self):
        last_index = len(self.A) - 1
        if last_index < 1:
            return None
        self.A[1], self.A[last_index] = self.A[last_index], self.A[1]
        min_key = self.A.pop()
        self.__min_heapify(1)
        return min_key
        

    def insert_key(self, key):
        self.A.append(key)
        check_index = len(self.A) - 1
        parent_index = int(check_index/2)
        self.__parent_updatify(parent_index, check_index)
        

    def __parent_updatify(self, parent_index, check_index):
        while parent_index >=1 and self.A[parent_index] > self.A[check_index]:
            self.A[parent_index], self.A[check_index] = self.A[check_index], self.A[parent_index]
            check_index, parent_index = parent_index, int(parent_index/2)


    def update_key(self, key, new_key):
        key_index = self.find_key(key)
        self.A[key_index] = new_key
        if not self.__min_heapify(key_index):
            self.__parent_updatify(int(key_index/2), key_index)
        
            
    def find_key(self, key):
        """
        Returns index of key in array (self.A). Uses BFS.
        """
        from queue import Queue
        qu = Queue()
        qu.put(1)
        key_index = None

        while not qu.empty():
            element = qu.get_nowait()
            if self.A[element] == key:
                key_index = element
                break
            left, right = element*2, element*2+1
            if left < len(self.A) and self.A[left] <= key:
                qu.put_nowait(left)
            if right < len(self.A) and self.A[right] <= key:
                qu.put_nowait(right)
        else:
            print("Key {0} not found".format(key))
        
        del(qu)
        return key_index
    

