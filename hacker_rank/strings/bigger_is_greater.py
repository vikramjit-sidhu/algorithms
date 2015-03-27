"""
Hacker Rank - Bigger is greater
https://www.hackerrank.com/challenges/bigger-is-greater
"""
    
def find_succ(char, char_freq):
    """ Find next lexicographical character to char """
    for i in range(ord(char)+1, 123):
        c1 = chr(i)
        if c1 in char_freq:
            return (True, c1)
    return (False, None)
    
def next_greatest_word(word):
    """ find lexicographically next greatest word to 'word' by rearranging its characters """
    new_word = ''
    char_freq = {word[-1]: 1}
    start_char = len(word) - 2  #starting from 2nd last character, as last char has already been processed
    for index in range(start_char, -1, -1):
        c1 = word[index]
        if c1 in char_freq:
            char_freq[c1] += 1
        else:
            char_freq[c1] = 1
        succ = find_succ(c1, char_freq)[1]
        if succ is not None:
            char_freq[succ] -= 1
            new_word = word[:index] + succ
            break
    else:
        return 'no answer'
    from string import ascii_lowercase
    for c2 in ascii_lowercase:
        if c2 in char_freq and char_freq[c2] > 0:
            new_word += c2*char_freq[c2]
    return new_word
    
def main():
    num_cases = int(input().strip())
    for i in range(num_cases):
        word = input().strip()
        print(next_greatest_word(word))
        
if __name__ == '__main__':
	main()