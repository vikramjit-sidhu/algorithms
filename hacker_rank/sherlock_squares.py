"""
Hacker Rank - Chocolate Feast
https://www.hackerrank.com/challenges/sherlock-and-squares

Find perfect squares in [a, b]
"""

from math import sqrt

number_status = {}  #hash containing the number and the boolean value as to whether it is a square

def check_square(n):
    """
    Check if n is a perfect square, done by two ways
    (using method described in wiki:
    http://en.wikipedia.org/wiki/Square_number
    1. See last digit of n it should be in [1, 4, 6, 9]
    2. The last two digits should be in [00, 25]
    """
    if n in number_status:
        return number_status[n]
    last_digit = n % 10
    last_two_digits = n % 100
    if (last_digit in (1, 4, 6, 9)) or (last_two_digits in (0, 25)):
        root = int(sqrt(n) + 0.5)
        if pow(root, 2) == n:
            number_status[n] = True
            return True
    number_status[n] = False
    return False

def count_squares(a, b):
    count_sq = 0
    for num in range(a, b+1):
        if check_square(num):
            count_sq += 1
    return count_sq
    
def main():
    test_cases = int(input().strip())
    for i in range(test_cases):
        a, b = [int(i) for i in input().strip().split(' ')]
        print(count_squares(a, b))

if __name__ == '__main__':
    main()