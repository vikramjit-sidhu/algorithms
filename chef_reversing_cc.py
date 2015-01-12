# chef and reversing code chef
# http://www.codechef.com/problems/REVERSE/

from collections import namedtuple

def main():
    n, m = [int(num) for num in input().strip().split(" ")]
    graph = create_graph(n, m)

    print(find_best_path(n, m, graph))



def find_best_path(n, m, graph):
    start_node = 1
    distance_table = dijkstra(n, m, graph, start_node)

    # print(graph, "\n")
    # print(distance_table)
    if distance_table[n].distance != float('inf'):
        no_reverses = int(distance_table[n].distance/999)
    else:
        no_reverses = -1
    return no_reverses



def dijkstra(vertices, edges, graph, start_node):
    DistanceTableEntry = namedtuple ('DistanceTableEntry', 'distance, parent')
    distance_table = [DistanceTableEntry(float('inf'), -2)] * (vertices+1)

    distance_table[int(start_node)] = distance_table[int(start_node)]._replace(distance=0, parent=-1)

    nodes_visited = []
    nodes_to_visit = []
    nodes_to_visit.append(int(start_node))

#starting dijkstra loop
    for node in nodes_to_visit:
        if graph[node]:     #if node has edges
            for node_to, distance in graph[node].items():
                dist = distance + distance_table[node].distance
                if distance_table[node_to].distance > dist:
                    distance_table[node_to] = distance_table[node_to]._replace(distance=dist, parent=node)

        nodes_visited.append(node)

        min_node = -2; min_distance = float('inf')

        all_nodes = list(range(1, vertices+1))
        nodes_left = [nod for nod in all_nodes if nod not in nodes_visited]
        for gray_node in nodes_left:
            if distance_table[gray_node].distance < min_distance:
                min_node = gray_node
                min_distance = distance_table[gray_node].distance

        if min_node != -2:
            nodes_to_visit.append(min_node)

    return distance_table




def create_graph(n, m):
    graph = [None] * (n+1)

    for z in range(m):
        efrom, eto = [int(num) for num in input().strip().split(" ")] #edge from and edge to

        if efrom == eto:
            continue
        elif graph[efrom]:
            if (eto in graph[efrom]) and (graph[efrom][eto] == 999):
                graph[efrom][eto] = 0.1
                continue
            elif (eto in graph[efrom]) and (graph[efrom][eto] == 0.1):
                continue
        
        if not graph[efrom]:
            graph[efrom] = {}
        graph[efrom][eto] = 0.1

        if not graph[eto]:
            graph[eto] = {}
        graph[eto][efrom] = 999

    return graph


if __name__ == '__main__':
    main()

