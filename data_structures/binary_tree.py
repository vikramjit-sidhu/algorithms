"""
basic binary tree implementation and traversal printing
"""

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

        
        
def main():
    root = Node(30)
    
    root.left = Node(15)
    root.left.left = Node(10)
    root.left.right = Node(20)
    
    root.right = Node(45)
    root.right.left = Node(40)
    root.right.right = Node(50)
    
    print("Inorder Traversal:")
    inorder(root)
    
    print("\nPostorder Traversal:")
    postorder(root)

    print("\nPreorder Traversal:")
    preorder(root)
    
    
def inorder(node):
    if node.left:
        inorder(node.left)
    print(node.key)
    if node.right:
        inorder(node.right)
    
    
def postorder(node):
    if node.left:
        postorder(node.left)
    if node.right:
        postorder(node.right)
    print(node.key)
    
 
def preorder(node):
    print(node.key)
    if node.left:
        preorder(node.left)
    if node.right:
        preorder(node.right)
    

if __name__ == '__main__':
	main()