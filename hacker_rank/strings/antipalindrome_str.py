"""
Hacker Rank - Antipalindromic Strings
https://www.hackerrank.com/challenges/antipalindromic-strings
"""

import sys

class TrieNode:
    def __init__(self):
        self.level = 0
        self.char = None
        self.prev_char = None
        self.word = ''
        self.children = {}

def set_recursion_depth(n):
    """ Changing the stack recursion depth of python, DO NOT TRY THIS AT HOME """
    if n > 1000:
        sys.setrecursionlimit(n+1)

def down_rabbit_hole(node, char_set, max_level):
    if node.level == max_level:
        return 1
    anti_palin = 0
    for char in char_set:
        if node.char != char and node.prev_char != char:
            new_node = TrieNode()
            new_node.level = node.level + 1
            new_node.char = char
            new_node.prev_char = node.char
            new_node.word = node.word + str(char)
            node.children[char] = new_node
            anti_palin += down_rabbit_hole(new_node, char_set, max_level)
    return anti_palin

def build_trie(root, char_set, max_level):
    curr_level, next_level = [root], []
    anti_palin = 0
    while len(curr_level) > 0:
        for node in curr_level:
            if node.level == max_level:
                anti_palin += 1
                continue
            for char in char_set:
                if node.char != char and node.prev_char != char:
                    new_node = TrieNode()
                    new_node.level = node.level + 1
                    new_node.char = char
                    new_node.prev_char = node.char
                    new_node.word = node.word + str(char)
                    node.children[char] = new_node
                    next_level.append(new_node)
        curr_level, next_level = next_level, []
    return anti_palin
    
def count_antipalindromes(m, n):
    # num = pow(10,9) + 7
    character_set = list(range(1, m+1))
    root = TrieNode()
    set_recursion_depth(n)
    num_anti_palins = down_rabbit_hole(root, character_set, n)
    # num_anti_palins = build_trie(root, character_set, n)
    return (num_anti_palins)

def main():
    num_cases = int(input().strip())
    for i in range(num_cases):
        #m -> size of alphabet set (consider a new alphabet set whose size can be greater than 26)
        #n -> length of strings
        n, m = (int(i) for i in input().strip().split(' '))
        print(count_antipalindromes(m, n))
        
if __name__ == '__main__':
    main()