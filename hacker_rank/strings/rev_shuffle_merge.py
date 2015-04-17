"""
Hacker Rank - Reverse Shuffle Merge
https://www.hackerrank.com/challenges/reverse-shuffle-merge
"""

import copy

class TrieNode:
    def __init__(self):
        self.word = ''
        self.leaf = False
        self.char_freq = {} #the char remaining for node to create
        self.children = {}


def get_char_freq(word):
    char_freq = {}
    for char in word:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    return char_freq
    
def insert_in_trie(char, root):
    """ While inserting a node into trie, all nodes who can accept that char acc to their char_freq have to have be traversed """
    curr_level, next_level = [root], []
    while len(curr_level) > 0:
        for node in curr_level:
            next_level.extend(node.children.values())
            if (node.char_freq[char] >= 1) and (char not in node.children):
                new_node = TrieNode()
                new_node.word = node.word + char
                new_node.char_freq = copy.deepcopy(node.char_freq)
        curr_level, next_level = next_level, []
    return root

def build_trie(char_freq, word):
    root = TrieNode()
    root.char_freq = copy.deepcopy(char_freq)
    for char in word:
        root = insert_in_trie(char, root)
    return root
    
def find_base_str(string):
    #Note: the char freq returned is the overall char freq of string div by 2.
    #since shuffle and reverse have the same char, the total char freq will be doubled.
    char_freq = get_char_freq(string)
    char_freq = {key:(val//2) for key, val in char_freq.items()}
    root = build_trie(char_freq, string)

def main():
    string = input().strip()
    print(find_base_str(string))

if __name__ == '__main__':
    main()