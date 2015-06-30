"""
Hacker Rank - Depth First Search, Prob of Reach
https://www.hackerrank.com/challenges/dfsprobreach
"""

from decimal import Decimal

can_reach = {}

def get_prob(num_nodes, graph, prob_list):
    """ 
    Find prob of reaching (num_nodes+1)th node from all other nodes 
    Add the prob of individual nodes
    """
    global can_reach
    can_reach[num_nodes+1] = True   #setting to true the reachability for the last node
    total_prob = 0
    for node in range(1, num_nodes+1):
        if reachable(node, graph):
            total_prob += prob_list[node-1]
    return total_prob
    
def reachable(node, graph):
    global can_reach
    if node not in can_reach:
        for adj_nodes in graph[node]:
            if reachable(adj_nodes, graph):
                can_reach[node] = True
                break
        else:
            can_reach[node] = False
    return can_reach[node]

def get_prob_reloaded(num_nodes, graph, prob_list):
    """
    --Do--
    """
    global can_reach
    can_reach[num_nodes+1] = True
    total_prob = Decimal(0)
    for node in range(1, num_nodes+1):
        if node in can_reach:
            if can_reach[node]:
                total_prob += prob_list[node-1]
            continue
        nodes_visited, nodes_tovisit = [], []
        nodes_tovisit.extend(graph[node])
        nodes_visited.append(node)
        for nd in nodes_tovisit:
            if nd in can_reach and can_reach[nd]:
                for nd_done in nodes_visited:
                    can_reach[nd_done] = True
                total_prob += prob_list[node-1]
                break
            else:
                for nd_poss in graph[nd]:
                    if nd_poss not in nodes_visited:
                        nodes_tovisit.append(nd_poss)
            nodes_visited.append(nd)
        if node not in can_reach:
            for nd_done in nodes_visited:
                can_reach[nd_done] = False
    return int(total_prob)
                
    
def main():
    num_cases = int(input().strip())
    for i in range(num_cases):
        num_nodes = int(input().strip())
        graph = {}
        for j in range(1, num_nodes+2):
            node_line = [int(i) for i in input().strip().split(' ')]
            graph[j] = []
            for node_to in node_line[1:]:
                #not adding self loops
                if node_to == j:
                    continue
                graph[j].append(node_to)
        prob_list = [Decimal(i) for i in input().strip().split(' ')]
        print((get_prob_reloaded(num_nodes, graph, prob_list)))

if __name__ == '__main__':
    main()