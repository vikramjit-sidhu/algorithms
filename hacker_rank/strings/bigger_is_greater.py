"""
Hacker Rank - Bigger is greater
https://www.hackerrank.com/challenges/bigger-is-greater
"""

def find_char_freq(word):
    """ given a word, return hash containing its char, freq """
    char_freq = {}
    for char in word:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    return char_freq

def next_greatest_word(word):
    """ find lexicographically next greatest word to 'word' by rearranging its characters """
    char_freq = find_char_freq(word)
    next_best = ''
    for char in word:
        char_freq[char] -= 1
        #find if there is a char lexicographically less than or eq to char in char_freq hash (encapsulate in function?)
        for i in range(ord(char), ord('a')-1, -1):
            #inside this for loop, the character (less than or equal to is found and we can append char to next_best
            c1 = chr(i)
            if c1 in char_freq:
                next_best += char
                break
        else:
            #finding the next greatest character lexicographically to char and appending it to string
            for j in range(ord(char)+1, ord('z')+1):
                c2 = chr(j)
                if c2 in char_freq:
                    char_freq[c2] -= 1
                    next_best += c2 + char
                    break
            else:
                #if we could not find any character greater than char, no solution possible
                return 'no answer'
            break   #breaking out of main for loop (line 20)
    #appending the reamaining characters to next_best in lexicographica order (starting from the num of 'a' left, then num of 'b' left, etc)
    for i in range(ord('a'), ord('z') + 1):
        c3 = chr(i)
        if c3 in char_freq:
            char_freq[c3] = 0
            next_best += c3*char_freq[c3]
    return next_best

def main():
    num_cases = int(input().strip())
    for i in range(num_cases):
        word = input().strip()
        print(next_greatest_word(word))
        
if __name__ == '__main__':
	main()