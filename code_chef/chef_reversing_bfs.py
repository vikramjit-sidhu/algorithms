"""
Chef and reversing, BFS implementation
http://www.codechef.com/problems/REVERSE/
"""

def bfs(vertices, edges, graph, start_node):
    from queue import Queue
    node_queue = Queue()
    distance_table = {}
    distance_table[start_node] = 0
    #putting initial node in bfs queue
    node_queue.put_nowait(start_node)
    #populating entries of distance_table
    for i in range(2, vertices+1):
        distance_table[i] = float("inf")
    while not node_queue.empty():
        node = node_queue.get_nowait()
        if graph[node] is not None: #check if node has vertices
            for node_to, distance in graph[node].items():
                dist = distance_table[node] + distance
                if dist < distance_table[node_to]:
                    distance_table[node_to] = dist
    return distance_table
                    
def find_best_path(n, m, graph):
    start_node = 1
    distance_table = bfs(n, m, graph, start_node)
    if distance_table[n] == float('inf'):
        return -1
    return int(distance_table[n])

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
    no_reverses = find_best_path(n, m, graph)
    print(no_reverses)

if __name__ == '__main__':
    main()