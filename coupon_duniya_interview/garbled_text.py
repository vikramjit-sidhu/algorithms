# Complete the function below.


class TrieNode:
    def __init__(self):
        self.char = ''
        self.the_end = False
        self.children = {}

def  findBabyWords( baby_words,  garbled_text):
    root = TrieNode()
    for word in baby_words:
        node, new_node = root, None
        for char in word:
            if char not in node.children:
                new_node = TrieNode()
                new_node.char = char
                node.children[char] = new_node
            else:
                new_node = node.children[char]
            node = new_node
        node.the_end = True
    act_words, tmp_word = '', ''
    node = root
    for char in garbled_text:
        if char in node.children:
            tmp_word += char
            node = node.children[char]
        else:
            if node.the_end:
                act_words += tmp_word + ' '
            tmp_word = ''
            node = root    
    print(act_words)

_baby_words_cnt = int(raw_input())
_baby_words_i=0
_baby_words = []
while _baby_words_i < _baby_words_cnt:
    _baby_words_item = raw_input()
    _baby_words.append(_baby_words_item)
    _baby_words_i+=1
    


_garbled_text = raw_input()

findBabyWords(_baby_words, _garbled_text);