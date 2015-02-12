"""
Binary Search Tree
"""


class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        
    def clean(self):
        self.left = None
        self.right = None
        self.parent = None
        
        
class BST:
    def __init__(self):
        self.root = None
        
    def insert(self, elt):
        if isinstance(elt, BSTNode):
            new_node = elt.clean()
        else:
            new_node = BSTNode(elt)
        #find position in tree to insert new_node
        if self.root is None:
            self.root = new_node
            return
        node = self.root
        while True:
            if node.key > new_node.key:
                if node.left:
                    node = node.left
                    continue
                else:
                    node.left = new_node
                    new_node.parent = node
                    break
            else:   #node.key <= key_insert
                if node.right:
                    node = node.right
                    continue
                else:
                    node.right = new_node
                    new_node.parent = node
                    break
                    
    def search(self, elt):
        if isinstance(elt, BSTNode):
            s_key = elt.key
        else:
            elt = s_key
        node = self.root
        while node:
            if s_key == node.key:
                print("Found key: {0}".format(s_key))
                break
            elif s_key > node.key:
                node = node.right
            else:
                node = node.left
        return node
    
    def delete(self, elt):
        node_del = self.search(elt)
        #trivial cases (only one child) handled in if and elif
        if (node.left is None) or (node.right is None):
            self._trivial_del(node)
        else:
            succ = find_successor(node)
            if succ.right is not None:
                succ = self._trivial_del(succ)
            father = node.parent
            if node is father.left:
                father.left = succ
            else:
                father.right = succ
            succ.parent = father
            succ.left = node.left
            succ.right = node.right
            node.right.parent = succ
            node.left.parent = succ
            
    def _trivial_del(self, node):
        if node.left is None:
            father = node.parent
            if node is father.left:
                father.left = node.right
            else:
                father.right = node.right
            if node.right:
                node.right.parent = father
        else:
            father = node.parent
            if node is father.left:
                father.left = node.left
            else:
                father.right = node.left
            node.left.parent = father
        node.clean()
        return node
    
    def find_successor(self, node):
        if node.right:
            succ = find_min(node.right)
        else:
            while (node.parent is not None) and (node is node.parent.right):
                node = node.parent
            succ = node.parent
        return succ
        
    def find_predecessor(self, node):
        if node.left:
            pred = find_max(node.right)
        else:
            while (node.parent is not None) and (node is node.parent.left):
                node = node.parent
            pred = node.parent
        return pred
    
    def find_min(self):
        print(self._find_min(self.root).key)
        
    def _find_min(self, node):
        while node.left:
            node = node.left
        return node
        
    def find_max(self):
        print(self._find_max(self.root).key)
        
    def _find_max(self, node):
        while node.right:
            node = node.right
        return node
    
    def inorder_rec(self):
        self._inorder_rec(self.root)
        
    def _inorder_rec(self, node):
        if node:
            self._inorder_rec(node.left)
            print(node.key)
            self._inorder_rec(node.right)
    
    def preorder(self):
        self._preorder(self.root)
        
    def _preorder(self, node):
        if node:
            print(node.key)
            self._preorder(node.left)
            self._preorder(node.right)
            
    def postorder(self):
        self._preorder(self.root)
        
    def _postorder(self, node):
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.key)
            
            
