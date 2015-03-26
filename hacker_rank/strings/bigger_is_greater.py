"""
Hacker Rank - Bigger is greater
https://www.hackerrank.com/challenges/bigger-is-greater
"""
import pdb
def find_char_freq(word):
    """ given a word, return hash containing its char, freq """
    char_freq = {}
    for char in word:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    return char_freq

def find_lesser_char(char, char_freq):
    """ Find if there is a character lexicographically lesser to char in char_freq hash """
    for i in range(ord(char), ord('a')-1, -1):
        c1 = chr(i)
        if c1 in char_freq and char_freq[c1] > 0:
            return True
    return False
    
def next_greatest_char(char, char_freq):
    """ Find the next greatest lexicographic character to char in char_freq """
    for j in range(ord(char)+1, ord('z')+1):
        if chr(j) in char_freq:
            return chr(j)
    return False
    
def next_greatest_word(word):
    """ find lexicographically next greatest word to 'word' by rearranging its characters """
    pdb.set_trace()
    char_freq = find_char_freq(word)
    next_best = ''
    for char in word:
        char_freq[char] -= 1
        if find_lesser_char(char, char_freq):
            next_best += char
        else:
            #finding the next greatest character lexicographically to char and appending it to string
            next_char = next_greatest_char(char, char_freq)
            if next_char is not False:
                char_freq[next_char] -= 1
                next_best += next_char + char
            else:
                #if we could not find any character greater than char, no solution possible
                return 'no answer'
            break
    #appending the reamaining characters to next_best in lexicographica order (starting from the num of 'a' left, then num of 'b' left, etc)
    for i in range(ord('a'), ord('z') + 1):
        c3 = chr(i)
        if c3 in char_freq and char_freq[c3] > 0:
            next_best += c3*char_freq[c3]
            char_freq[c3] = 0
    return next_best

def main():
    num_cases = int(input().strip())
    for i in range(num_cases):
        word = input().strip()
        print(next_greatest_word(word))
        
if __name__ == '__main__':
	main()