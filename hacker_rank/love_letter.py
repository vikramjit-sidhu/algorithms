"""
Hacker rank question: Love letter mystery
https://www.hackerrank.com/challenges/the-love-letter-mystery
"""

def find_palindrome(word):
    first_index = 0
    end_index = len(word) - 1
    oper_req = 0
    while first_index < end_index:
        if word[first_index] == word[end_index]:
            first_index += 1
            end_index -= 1
            continue
        ascii_first = ord(word[first_index])
        ascii_last = ord(word[end_index])
        oper_req += abs(ascii_first - ascii_last)
        first_index += 1
        end_index -= 1
    return oper_req

def main():
    test_cases = int(input().strip())
    for i in range(test_cases):
        word = input().strip()
        print(find_palindrome(word))

if __name__ == '__main__':
    main()