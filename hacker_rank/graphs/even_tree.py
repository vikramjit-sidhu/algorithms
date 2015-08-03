"""
Hacker Rank - Even Tree
https://www.hackerrank.com/challenges/even-tree
"""

class TreeNode:
    def __init__(self):
        self.key = 0
        # the number of nodes contained in all subtrees of this node
        # includes the current node in count
        self.nodes = 1  # only include current node value initially
        self.parent = None
        self.children = []


def main():
    num_vertices, num_edges = (int(i) for i in input().strip().split(' '))
    

if __name__ == "__main__":
    main()