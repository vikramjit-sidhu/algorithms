"""
Hacker Rank - Chocolate Feast
https://www.hackerrank.com/challenges/sherlock-and-squares

Find perfect squares in [a, b]
"""

from math import sqrt, ceil, floor

def count_squares(a, b):
    """ 
    Using logic, that number of integers in range ceiling(sqrt(a)) and floor(sqrt(b))
    is the number of integers that have a perfect square
    """
    lower_lt = ceil(sqrt(a))
    upper_lt = floor(sqrt(b))
    count_sq = upper_lt - lower_lt + 1
    return count_sq
    
def main():
    test_cases = int(input().strip())
    for i in range(test_cases):
        a, b = [int(i) for i in input().strip().split(' ')]
        print(count_squares(a, b))

if __name__ == '__main__':
    main()