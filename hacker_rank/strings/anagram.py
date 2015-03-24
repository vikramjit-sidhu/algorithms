"""
Hacker Rank - Anagram
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
    num_cases = int(input().strip())
    for i in range(num_cases):
        word = input().strip()
        mid = len(word) // 2
        str1 = word[:mid]
        str2 = word[mid:]
        if len(str1) != len(str2):
            print(-1)
            continue
        char_freq1 = get_char_freq(str1)
        char_freq2 = get_char_freq(str2)
        common_chars = find_common_chars(char_freq1, char_freq2)
        print(min(len(str1)-common_chars, len(str2)-common_chars))

if __name__ == '__main__':
    main()