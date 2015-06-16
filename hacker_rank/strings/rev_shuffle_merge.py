"""
Hacker Rank - Reverse Shuffle Merge
https://www.hackerrank.com/challenges/reverse-shuffle-merge
"""

import copy, string

class DAGNode:
    def __init__(self, char):
        self.char = char
        self.children = {}  #each child contains a list of the possible nodes, e.g {'a': [Node1, Node2], .. }
        self.char_freq = {} #char freq of the words which come after this node

def get_char_freq(word):
    char_freq = {}
    for char in word:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    return char_freq
    
def create_dag(word):
    """
    Creates a DAG with each letter pointing to all the letters following it.
    """
    node = DAGNode(word[-1])
    node.char_freq[word[-1]] = 1
    for char in word[-2::-1]:   #start from 2nd last word, and use a -1 step, so traverse the char in reverse order
        #create a new DAG node which is the successor of 'node'
        new_node = DAGNode(char)
        #copy attributes of node into new_node
        new_node.children = copy.deepcopy(node.children)
        new_node.char_freq = copy.deepcopy(node.char_freq)
        #add char of node into its char_freq, char_freq represents the characters and their freq which come after new_node
        if char in new_node.char_freq:
            new_node.char_freq[char] += 1
        else:
            new_node.char_freq[char] = 1
        #add node into new_node's children
        if node.char in new_node.children:
            new_node.children[node.char].insert(0, node)
        else:
            new_node.children[node.char] = [node]
        node, new_node = new_node, None
    root = DAGNode(char)
    root.children = copy.deepcopy(node.children)
    root.char_freq = copy.deepcopy(node.char_freq)
    if node.char in root.children:
        root.children[node.char].insert(0, node)
    else:
        root.children[node.char] = [node]
    return root
    
def find_lex_greatest(root, char_freq):
    """
    Given a DAG of reversed and spliced words, find a lexicographically greatest word which has char_freq characters and count
    """
    node = root #current node being processed
    word = ''
    while(True):
        if not char_freq:
            break
        for char in sorted(char_freq.keys(), reverse=True):
            if char in node.children:
                possible_next_node = node.children[char][0]
                #compare the char_freq of possible_next_node and char_freq
                for chr in char_freq.keys():
                    if chr not in possible_next_node.char_freq or possible_next_node.char_freq[chr] < char_freq[chr]:
                        break
                else:
                    node = possible_next_node
                    word += node.char
                    if char_freq[node.char] > 1:
                        char_freq[node.char] -= 1
                    else:
                        del char_freq[node.char]
                    break
    return word   
    
def find_base_str(string):
    #Note: the char freq returned is the overall char freq of string, we divide by 2 to get actual char freq.
    #since shuffle and reverse have the same char, the total char freq will be doubled.
    char_freq = get_char_freq(string)
    char_freq = {key:(val//2) for key, val in char_freq.items()}
    root = create_dag(string)
    rev_word = find_lex_greatest(root, char_freq)
    return rev_word[::-1]
    
def main():
    string = input().strip()
    print(find_base_str(string))

if __name__ == '__main__':
    main()