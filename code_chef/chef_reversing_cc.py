# chef and reversing code chef
# http://www.codechef.com/problems/REVERSE/

from collections import namedtuple



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




def dijkstra(vertices, edges, graph, start_node):
    DistanceTableEntry = namedtuple ('DistanceTableEntry', 'distance, parent')
    distance_table = [DistanceTableEntry(float('inf'), -2)] * (vertices+1)

    distance_table[int(start_node)] = distance_table[int(start_node)]._replace(distance=0, parent=-1)

    priority_queue = MinHeap()
    priority_queue.insert_key((0, start_node))
    for i in range(2, vertices+1):
        priority_queue.insert_key((float("inf"), i))
    #node is a tuple of form (distance entry in distance table, node index in graph)
        
    #starting dijkstra loop
    last_vertice = vertices-1
    node = priority_queue.extract_min()
    while node:
        if graph[node[1]]:     #if node has edges
            for node_to, distance in graph[node[1]].items():
                dist = distance + distance_table[node[1]].distance
                if distance_table[node_to].distance > dist:
                    priority_queue.update_key((distance_table[node_to].distance, node_to), (dist, node_to))
                    distance_table[node_to] = distance_table[node_to]._replace(distance=dist, parent=node)
        node = priority_queue.extract_min()
        if node == last_vertice:
            break
                
    return distance_table


def find_best_path(n, m, graph):
    start_node = 1  #start from node 1 not 0.
    distance_table = dijkstra(n, m, graph, start_node)

    if distance_table[n].distance != float('inf'):
        no_reverses = int(distance_table[n].distance)
    else:
        no_reverses = -1
    return no_reverses


def create_graph(n, m):
    """
    Graph has vertices, numbered from 1 to N, the 0th index may be created but is never used
    m is number of edges
    """
    graph = [None] * (n+1)
    for_edge = 0
    rev_edge = 1
    
    for z in range(m):
        efrom, eto = [int(num) for num in input().strip().split(" ")] #edge from and edge to

        if efrom == eto:
            continue
        elif graph[efrom]:
            if (eto in graph[efrom]) and (graph[efrom][eto] == rev_edge):
                graph[efrom][eto] = for_edge
                continue
            elif (eto in graph[efrom]) and (graph[efrom][eto] == for_edge):
                continue
        
        if not graph[efrom]:
            graph[efrom] = {}
        graph[efrom][eto] = for_edge

        if not graph[eto]:
            graph[eto] = {}
        graph[eto][efrom] = rev_edge

    return graph

    
def main():
    n, m = [int(num) for num in input().strip().split(" ")]
    graph = create_graph(n, m)

    print(find_best_path(n, m, graph))
    

if __name__ == '__main__':
    main()

