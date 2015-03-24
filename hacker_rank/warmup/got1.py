"""
Hacker Rank - Algorithms, Warmup
Game of thrones 1
https://www.hackerrank.com/challenges/game-of-thrones
"""

def check_palindrome(word):
    """ Check if there exists an anagram of 'word' which is a palindrome.
    Assuming that a palindrome has characters which occur an even number of times, 
    or one character occurring an odd number of times"""
    char_count = {} #char count hash
    for char in word:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    odd_count = 0   #counting number of odd nos encountered
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1
    len_word = len(word)
    if len_word % 2 == 0:
        if odd_count >= 1:
            return False
    else:
        if odd_count > 1:
            return False
    return True
            
def main():
    word = input().strip()
    if check_palindrome(word):
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
	main()