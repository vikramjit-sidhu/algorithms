"""
Hacker Rank - Sherlock and Anagrams
https://www.hackerrank.com/challenges/sherlock-and-anagrams
"""

import copy

class TrieNode:
    def __init__(self):
        self.word = ''
        self.count = 0  #the number of times this character/substring appears in the word
        self.char_freq = {}
        self.children = {}


fact_hash = {}
        
def build_trie(word):
    root = TrieNode()
    for index, char in enumerate(word):
        if char in root.children:
            curr_node = root.children[char]
            curr_node.count += 1
        else:
            curr_node = TrieNode()
            curr_node.word = char
            curr_node.count += 1
            curr_node.char_freq[char] = 1
            root.children[char] = curr_node
        for char2 in word[index+1:]:
            if char2 in curr_node.children:
                curr_node = curr_node.children[char2]
                curr_node.count += 1
            else:
                next_node = TrieNode()
                next_node.word = curr_node.word + char2
                next_node.count += 1
                next_node.char_freq = copy.deepcopy(curr_node.char_freq)
                if char2 in next_node.char_freq:
                    next_node.char_freq[char2] += 1
                else:
                    next_node.char_freq[char2] = 1
                curr_node.children[char2] = next_node
                curr_node = next_node
    return root

def factorial(num):
    """ Returns factorial of num. Uses global hash fact_hash to save time. """
    fact = 1
    for i in range(num, 0, -1):
        if i in fact_hash:
            fact_hash[num] = fact*fact_hash[i]
            return fact_hash[num]
        fact *= i
    fact_hash[num] = fact
    return fact
    
def calculate_combinations(num):
    """ Given a substring occurring num times, we find the ways it can be extracted 2 at a time. """
    return (factorial(num)//(2*factorial(num-2)))
    
def count_anagramic_substrings(word):
    #first build a trie with all the substrings possible in word
    root = build_trie(word)
    #now doing a breadth first search of the trie nodes, only the nodes on the same level can be anagramic substrings
    #nodes(substrings) on the same level are compared by their char_freq, they should match for anagrams
    num_anagrams = 0
    curr_level, next_level = [], []
    #populating level 0
    curr_level.extend(list(root.children.values()))
    while len(curr_level) > 0:
        # print('\nlevel up, num_anagrams: ', num_anagrams)
        for index, node in enumerate(curr_level):
            # print("{}: {}".format(node.word, node.count))
            next_level.extend(list(node.children.values()))
            if node.count >= 2:
                num_anagrams += calculate_combinations(node.count)
            #compare node with all the other nodes
            for node2 in curr_level[index+1:]:
                if node2.char_freq == node.char_freq:
                    # print(' matched: ', node.word, node2.word)
                    num_anagrams += 1
        curr_level, next_level = next_level, []
    return num_anagrams

def main():
    num_cases = int(input().strip())
    for i in range(num_cases):
        word = input().strip()
        print(count_anagramic_substrings(word))

if __name__ == '__main__':
    main()