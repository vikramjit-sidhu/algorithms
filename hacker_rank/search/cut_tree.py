"""
Hacker Rank - Cut the tree
https://www.hackerrank.com/challenges/cut-the-tree
"""

class TreeNode:
    def __init__(self, val=0):
       self.value = val
       self.tot_value = None
       self.parent = None
       self.children = []


def populate_total_height(node):
    # pdb.set_trace()
    if not node.children:
        node.tot_value = node.value
        return
    val = node.value
    for child in node.children:
        if child.tot_value is None:
            populate_total_height(child)
        val += child.tot_value
    node.tot_value = val

def find_edge_remove(num_nodes, root):
    populate_total_height(root)
    min_diff = float('inf')
    total_height = root.tot_value
    nodes_tovisit = [root]
    for curr_node in nodes_tovisit:
        for child in curr_node.children:
            other_subtr = total_height - child.tot_value
            diff = abs(child.tot_value - other_subtr)
            if diff < min_diff:
                min_diff = diff
            nodes_tovisit.append(child)
    return min_diff

def main():
    num_nodes = int(input().strip())
    node_vals = [int(i) for i in input().strip().split(' ')]
    nodes = []
    for val in node_vals:
        node = TreeNode(val)
        nodes.append(node)
    for i in range(num_nodes-1):
        node1, node2 = (int(i) for i in input().strip().split(' '))
        node1, node2 = node1-1, node2-1 #indexing it acc to how it is in nodes list
        if nodes[node2].parent is not None:
            nodes[node2].children.append(nodes[node1])
            nodes[node1].parent = nodes[node2]
        else:
            nodes[node1].children.append(nodes[node2])
            nodes[node2].parent = nodes[node1]
    root = nodes[0]
    print(find_edge_remove(num_nodes, root))

if __name__ == '__main__':
    main()