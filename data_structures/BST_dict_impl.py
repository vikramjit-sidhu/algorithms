"""
BST implementation using Dictionaries
This assumes that each key is unique, else implementation will fail
Each entry in dictionary contains a list with 1st element as left node and 2nd
element as right node. Last element is parent
tree = { ...
    node_key : [node's left child, node's right child, node's parent]
  ...  }
  
DELETION NOT DONE
"""

class BST:
    def __init__(self):
        self.root = None
        self.tree = {}
        
    def insert(self, key):
        if self.root is None:
            self.root = key
            self.tree[key] = [None, None, None]
            return key
        node = self.root
        while node is not None:
            if node < key:  #go down left subtree
                if self.tree[node][0] is not None:
                    node = self.tree[node][0]
                else:
                    self.tree[node][0] = key
                    self.tree[key] = [None, None, node]
                    break
            else:   #go down right subtree
                if self.tree[node][1] is not None:
                    node = self.tree[node][1]
                else:
                    self.tree[node][1] = key
                    self.tree[key] = [None, None, node]
                    break
        return key
                    
    def search(self, key):
        if key in self.tree:
            return True
        else:
            return False


