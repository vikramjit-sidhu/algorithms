"""
Hacker Rank - Connected Cells
https://www.hackerrank.com/challenges/connected-cell-in-a-grid
"""

def find_connections(rows, cols, matrix):
    graph, nodes_tovisit = create_graph(rows, cols, matrix)
    nodes_visited = {}
    # for nd,it in graph.items():
        # print('{0}: {1}'.format(nd, it))
    longest_len = 0
    for row, col in nodes_tovisit:
        if (row,col) not in nodes_visited:
            nodes_visited[(row,col)] = 1
        else:   #node has already been visited
            continue
        curr_len = 1
        curr_nodes = [] #nodes to visit in the current context
        curr_nodes.extend(graph[(row,col)])
        for i,j in curr_nodes:
            if (i,j) in nodes_visited:
                continue
            curr_len += 1
            nodes_visited[(i,j)] = 1
            curr_nodes.extend(graph[(i,j)])
        if curr_len > longest_len:
            longest_len, curr_len = curr_len, 0
    return longest_len

def create_graph(rows, cols, matrix):
    for row in matrix:
        #append 0 element to beginning and end of list
        row.insert(0,0)
        row.append(0)
    new_row = [0] * (cols+2)
    matrix.append(new_row)
    matrix.insert(0,new_row)
    # for row in matrix:
        # print(row)
    graph = {}
    nodes_tovisit = []
    for i in range(1, rows+1):
        for j in range(1, cols+1):
            if matrix[i][j] == 1:
                nodes_tovisit.append((i,j))
                if (i,j) not in graph:
                    graph[(i,j)] = []
                if matrix[i+1][j] == 1:
                    graph[(i,j)].append((i+1,j))
                    if (i+1,j) in graph:
                        graph[(i+1,j)].append((i,j))
                    else:
                        graph[(i+1,j)] = [(i,j)]
                if matrix[i][j+1] == 1:
                    graph[(i,j)].append((i,j+1))
                    if (i,j+1) in graph:
                        graph[(i,j+1)].append((i,j))
                    else:
                        graph[(i,j+1)] = [(i,j)]
                if matrix[i+1][j+1] == 1:
                    graph[(i,j)].append((i+1,j+1))
                    if (i+1,j+1) in graph:
                        graph[(i+1,j+1)].append((i,j))
                    else:
                        graph[(i+1,j+1)] = [(i,j)]
                if matrix[i+1][j-1] == 1:
                    graph[(i,j)].append((i+1,j-1))
                    if (i+1,j-1) in graph:
                        graph[(i+1,j-1)].append((i,j))
                    else:
                        graph[(i+1,j-1)] = [(i,j)]
    return graph, nodes_tovisit           
    
def main():
    rows = int(input().strip())
    cols = int(input().strip())
    matrix = []
    for i in range(rows):
        matrix.append([int(i) for i in input().strip().split(' ')])
    print(find_connections(rows, cols, matrix))
        
if __name__ == '__main__':
    main()