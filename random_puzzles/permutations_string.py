"""
Permutations of a string
"""

import copy

class TrieNode:
    def __init__(self):
        # self.parent = None
        self.word = None
        self.char_freq = {}
        # self.children = {}


def find_char_freq(word):
    char_freq = {}
    for char in word:
        if char not in char_freq:
            char_freq[char] = 1
        else:
            char_freq[char] += 1
    return char_freq

def find_perms(word):
    char_freq = find_char_freq(word)
    curr_level, next_level = [], []
    final_perms = []
    root = TrieNode()
    root.word = ''
    root.char_freq = char_freq
    curr_level.append(root)
    while curr_level:
        for node in curr_level:
            if not node.char_freq:
                final_perms.append(node.word)
            else:
                for char in node.char_freq.keys():
                    new_node = TrieNode()
                    new_node.word = node.word + char
                    new_node.char_freq = copy.copy(node.char_freq)
                    if new_node.char_freq[char] == 1:
                        del new_node.char_freq[char]
                    else:
                        new_node.char_freq[char] -= 1
                    next_level.append(new_node)
        curr_level, next_level = next_level, []
    # print(final_perms)
    return len(final_perms)

def main():
    perm_str = input().strip()
    print(find_perms(perm_str))


if __name__ == '__main__':
    main()
