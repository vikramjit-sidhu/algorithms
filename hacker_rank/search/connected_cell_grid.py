"""
Hacker Rank - Connected Cells
https://www.hackerrank.com/challenges/connected-cell-in-a-grid
"""

def find_connections(rows, cols, matrix):
    graph = create_graph(rows, cols, matrix)
    print(graph)

def create_graph(rows, cols, matrix):
    for row in matrix:
        row.append(0)
    new_row = [0] * cols
    graph = {}
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                if matrix[i+1][j] == 1:
                    if (i,j) in graph:
                        graph[(i,j)].append((i+1,j))
                    else:
                        graph[(i,j)] = [(i+1,j)]
                    if (i+1,j) in graph:
                        graph[(i+1,j)].append((i,j))
                    else:
                        graph[(i+1,j)] = [(i,j)]
                if matrix[i][j+1] == 1:
                    if (i,j) in graph:
                        graph[(i,j)].append((i,j+1))
                    else:
                        graph[(i,j)] = [(i,j+1)]
                    if (i,j+1) in graph:
                        graph[(i,j+1)].append((i,j))
                    else:
                        graph[(i,j+1)] = [(i,j)]
                if matrix[i+1][j+1] == 1:
                    if (i,j) in graph:
                        graph[(i,j)].append((i+1,j+1))
                    else:
                        graph[(i,j)] = [(i+1,j+1)]
                    if (i,j+1) in graph:
                        graph[(i+1,j+1)].append((i,j))
                    else:
                        graph[(i+1,j+1)] = [(i,j)]
    return graph            
    
def main():
    rows = int(input().strip())
    cols = int(input().strip())
    matrix = []
    for i in range(rows):
        matrix.append([int(i) for i in input().strip().split(' ')])
    find_connections(rows, cols, matrix)
        
if __name__ == '__main__':
    main()