"""
Palindrome index
https://www.hackerrank.com/challenges/palindrome-index
"""

def remove_err_char(word):
    start, end = 0, len(word)-1
    index_remove = -1
    alt_index = -1
    while start < end:
        if word[start] != word[end]:
            if index_remove != alt_index:
                return alt_index
            if word[start+1] == word[end] and word[start] == word[end-1]:
                index_remove = start
                alt_index = end
                start += 1
                continue
            elif word[start+1] == word[end]:
                index_remove = start
                break
            elif word[end-1] == word[start]:
                index_remove = end
                break
            else:
                print('WORLD HAS ENDED, INCORRECT INPUT')
                break
        start, end = start+1, end-1
    return index_remove

def main():
    num_cases = int(input().strip())
    for i in range(num_cases):
        word = input().strip()
        print(remove_err_char(word))    #returns index of char to be removed

if __name__ == '__main__':
    main()