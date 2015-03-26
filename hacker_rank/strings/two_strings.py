"""
Hacker Rank - Two strings
https://www.hackerrank.com/challenges/two-strings
"""

def check_substring(word1, word2):
    char_hash = {}  #hash containing all characters in word1, count of characters is not maintained
    for char in word1:
        if char not in char_hash:
            char_hash[char] = True
    for char in word2:
        if char in char_hash:
            return 'YES'
    return 'NO'

def main():
    num_cases = int(input().strip())
    for i in range(num_cases):
        word1 = input().strip()
        word2 = input().strip()
        print(check_substring(word1, word2))

if __name__ == '__main__':
	main()