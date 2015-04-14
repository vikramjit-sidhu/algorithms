"""
Number of anagram subsequences
"""

from queue import Queue
import copy

fact_hash = {}  #global variable fact_hash stores the factorials to save computation

class TrieNode:
    def __init__(self):
        self.children = {}
        self.char_freq_rem = {} #the remaining char (and freq) which can form more words
        self.word = ""
        self.distinct_words = -1 #this signifies that the count has not been calculated (as opposed to 0)

        
def find_char_freq(word):
    char_freq = {}
    for char in word:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    return char_freq
        
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
        
def distinct_words_count(word):
    """ 
    Given word, find all possible distinct words possible with the characters of word.
    Uses fomula from permutation, that given n characters of which k characters are repeating
    di -> represents the number of repetitions of the character
    fact(n)/(fact(d1)*fact(d2)...fact(dk))
    """
    n = len(word)
    char_freq = find_char_freq(word)
    prod = 1
    for freq in char_freq.values():
        if freq > 1:
            prod *= factorial(freq)
    num_distinct_words = factorial(n)//prod
    return num_distinct_words
        
def find_anagram_pairs(num_distinct_words):
    """ 
    Let n = num_distinct_words 
    total anagram pairs = n + nC2 (combination formula)
    """
    n = num_distinct_words
    anagram_pairs = n + factorial(n)//(factorial(n-2)*2)
    return anagram_pairs
    
def unordered_anagram_pairs(word):
    qu = Queue()
    char_freq = find_char_freq(word)
    tot_anagram_pairs = 0
    #initial setting up of values in queue, only taking all single char words
    for key, val in char_freq.items():
        if val >= 2:
            node = TrieNode()
            node.word = key
            char_freq[key] -= 2
            node.char_freq_rem = copy.deepcopy(char_freq)
            node.distinct_words = 1
            qu.put_nowait(node)
            
    #main building of trie. (without actually storing values in a trie)
    while not qu.empty():
        curr_node = qu.get_nowait()
        print("word: {}, distinct_words: {}".format(curr_node.word, curr_node.distinct_words))
        tot_anagram_pairs += find_anagram_pairs(curr_node.distinct_words)
        print("anagram pairs: ", find_anagram_pairs(curr_node.distinct_words))
        for key, val in curr_node.char_freq_rem.items():
            if val >= 2:
                node = TrieNode()
                node.word = curr_node.word + key
                curr_node.char_freq_rem[key] -= 2
                node.char_freq_rem = copy.deepcopy(curr_node.char_freq_rem)
                node.distinct_words = distinct_words_count(node.word)
                qu.put_nowait(node)
    return tot_anagram_pairs

def main():
    num_cases = int(input().strip())
    for i in range(num_cases):
        str_case = input().strip()
        print(unordered_anagram_pairs(str_case))

if __name__ == '__main__':
    main()