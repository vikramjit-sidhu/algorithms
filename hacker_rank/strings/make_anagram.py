"""
Hacker Rank - Make it anagram
https://www.hackerrank.com/challenges/make-it-anagram
"""

def get_char_freq(word):
    char_hash = {}
    for char in word:
        if char in char_hash:
            char_hash[char] += 1
        else:
            char_hash[char] = 1
    return char_hash
   
def find_common_chars(char_freq1, char_freq2):
    common_chars = 0
    for char, freq in char_freq1.items():
        if char in char_freq2:
            if freq > char_freq2[char]:
                common_chars += char_freq2[char]
            else:
                common_chars += freq
    return common_chars
   
def main():
    word1 = input().strip()
    word2 = input().strip()
    char_freq1 = get_char_freq(word1)
    char_freq2 = get_char_freq(word2)
    #finding common char and their number
    common_chars = find_common_chars(char_freq1, char_freq2)
    del_req = len(word1) + len(word2) - 2*common_chars
    print(del_req)

if __name__ == '__main__':
    main()