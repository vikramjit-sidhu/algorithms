"""
Hacker Rank - Reverse Shuffle Merge
https://www.hackerrank.com/challenges/reverse-shuffle-merge
"""

import copy, string

def get_char_freq(word):
    char_freq = {}
    for char in word:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    return char_freq
    
def find_base_str(string):
    #Note: the char freq returned is the overall char freq of string div by 2.
    #since shuffle and reverse have the same char, the total char freq will be doubled.
    char_freq = get_char_freq(string)
    char_freq = {key:(val//2) for key, val in char_freq.items()}
    rev_char_list, rank_char = rank_characters(char_freq)
    len_word = sum(char_freq.values())
    rev_word = gen_subsequence(string, len_word, sorted_char_list, rank_char)
    return rev_word[::-1]
    
def main():
    string = input().strip()
    print(find_base_str(string))

if __name__ == '__main__':
    main()