"""
Hacker Rank - Chocolate Feast
https://www.hackerrank.com/challenges/sherlock-and-squares

Find perfect squares in [a, b]
"""

from math import sqrt

def find_squares(a, b):
    count_sq = 0
    for num in range(a, b+1):
        tst = int(sqrt(num)+0.5)
        if pow(tst, 2) == num:
            count_sq += 1
    return count_sq
    
def main():
    test_cases = int(input().strip())
    for i in range(test_cases):
        a, b = [int(i) for i in input().strip().split(' ')]
        print(find_squares(a, b))

if __name__ == '__main__':
    main()