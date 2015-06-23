"""
Hacker Rank - Maximise Sum
https://www.hackerrank.com/challenges/maximise-sum
"""

class BST:
    def __init__(self):
        self.root = None    #just first element, not actual root
        self.max = None #keep track of max elt in tree
        self.tree = {}
        
    def insert(self, key):
        if self.root is None:
            self.root = key
            self.max = key
            self.tree[key] = True
            return
        if key > self.max:
            self.max = key
        self.tree[key] = True
    
    def get_max(self):
        return self.max
    
    def search(self, key):
        if key in self.tree:
            return True
        else:
            return False

def max_sum(size_list, mod_num, num_list):
    bst = BST()
    mod_list = []   #contains mod numbers from last iteration
    for num in num_list:
        mod_list = [(num+i)%mod_num for i in num_list]
        mod_list.append(num%mod_num)
        for num2 in mod_list:
            if not bst.search(num2):
                bst.insert(num2)
    return bst.get_max()

def main():
    num_cases = int(input().strip())
    for i in range(num_cases):
        size_list, mod_num = (int(i) for i in input().strip().split(' '))
        num_list = [int(i) for i in input().strip().split(' ')]
        print(max_sum(size_list, mod_num, num_list))

if __name__ == '__main__':
    main()