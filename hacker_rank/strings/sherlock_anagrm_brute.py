"""
Feeder program for sherlock and anagrams
Finding the number of substrings of a word and comparing them - brute force style, no trie used
"""

def create_substr_hash(word):
    substr_dict = {}    #storing the substrings in a hash with size of substr : list of substr pairs
    substr_dict[1] = []
    for index, char in enumerate(word):
        substr = char
        substr_dict[1].append(substr)
        len_substr = 1
        for char2 in word[index+1:]:
            substr += char2
            len_substr += 1
            if len_substr in substr_dict:
                substr_dict[len_substr].append(''.join(sorted(substr)))
            else:
                substr_dict[len_substr] = [''.join(sorted(substr))]
    return substr_dict

def count_anagramic_substrings(word):
    substr_dict = create_substr_hash(word)
    num_anagrams = 0
    #getting the list of substrings by length of substring
    for list_substr in substr_dict.values():
        #doing a brute force search on the substring list on each item
        for index, word in enumerate(list_substr):
            for word2 in list_substr[index+1:]:
                if word == word2:
                    print(word)
                    num_anagrams += 1
    return num_anagrams
        
def main():
    num_cases = int(input().strip())
    for i in range(num_cases):
        word = input().strip()
        print(count_anagramic_substrings(word))

if __name__ == '__main__':
    main()