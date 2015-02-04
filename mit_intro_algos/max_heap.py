"""
Creates a max heap, can also use heap sort algorithm on a pre created array
Uses an array to implement array
My implementation of python heapq module
"""

class MaxHeap:
    def __init__(self, ar=[None]):
        self.A = ar
        if len(self.A) > 1:
            self.__create_maxheap()


    def __max_heapify(self, index):
        left, right = 2*index, 2*index+1
        if left < len(self.A) and self.A[index] < self.A[left]:
            maximum = left
        else:
            maximum = index
        if right < len(self.A) and self.A[maximum] < self.A[right]:
            maximum = right
            
        if maximum != index:
            self.A[index], self.A[maximum] = self.A[maximum], self.A[index]
            self.__max_heapify(maximum)
            return True
        return False
        

    def __create_maxheap(self):
        if self.A[0]:
            self.A.append(self.A[0])
            self.A[0] = None
        start_index = int((len(self.A)-1)/2)
        for i in range(start_index, 0, -1):
            self.__max_heapify(i)
    

    def find_max(self):
        return self.A[1]
    

    def extract_max(self):
        last_index = len(self.A) - 1
        self.A[1], self.A[last_index] = self.A[last_index], self.A[1]
        max_key = self.A.pop()
        max_heapify(1)
        return max_key
        

    def insert_key(self, key):
        self.A.append(key)
        check_index = len(self.A) - 1
        parent_index = int(check_index/2)
        self.__parent_updatify(parent_index, check_index)
        

    def __parent_updatify(self, parent_index, check_index):
        while parent_index >=1 and self.A[parent_index] < self.A[check_index]:
            self.A[parent_index], self.A[check_index] = self.A[check_index], self.A[parent_index]
            check_index, parent_index = parent_index, int(parent_index/2)


    def update_key(self, key, new_key):
        key_index = self.find_key(key)
        self.A[key_index] = new_key
        if not self.__max_heapify(key_index):
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
            if left < len(self.A) and self.A[left] >= key:
                qu.put_nowait(left)
            if right < len(self.A) and self.A[right] >= key:
                qu.put_nowait(right)
        else:
            print("Key {0} not found".format(key))
        
        del(qu)
        return key_index
    



if __name__ == '__main__':
    main()