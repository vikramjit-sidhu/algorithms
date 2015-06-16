"""
Hacker Rank - Reverse Shuffle Merge
https://www.hackerrank.com/challenges/reverse-shuffle-merge
WRONG ALGO
"""

def lcs(a, b):
    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    # row 0 and column 0 are initialized to 0 already
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = \
                    max(lengths[i+1][j], lengths[i][j+1])
    # read the substring out from the matrix
    result = ""
    x, y = len(a), len(b)
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x-1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y-1]:
            y -= 1
        else:
            assert a[x-1] == b[y-1]
            result = a[x-1] + result
            x -= 1
            y -= 1
    return result

def get_char_freq(word):
    char_freq = {}
    for char in word:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    return char_freq
    
def generate_rev_word(string, char_freq):
    word = ''
    while char_freq:
        for char in sorted(char_freq.keys(), reversed=True):
            word += char
            if len(lcs(word, string)) == len(word):
                if char_freq[char] > 1:
                    char_freq[char] -= 1
                else:
                    del char_freq[char]
                continue
            else:
                word = word[:-1]
    return word

def find_base_str(string):
    char_freq = get_char_freq(string)
    char_freq = {key:(val//2) for key, val in char_freq.items()}
    rev_word = generate_rev_word(string, char_freq)

def main():
    string = input().strip()
    print(find_base_str(string))

if __name__ == '__main__':
    main()