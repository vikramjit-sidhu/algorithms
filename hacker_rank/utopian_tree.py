"""
Hacker rank challenge
Utopian tree
https://www.hackerrank.com/challenges/utopian-tree
"""
from math import pow

def find_growth(seasons):
    """
    Using pattern: 
    after season 0 ht = 2^1-1
    after season 1 ht = 2^2-1-1
    after season 2 ht = 2^2-1
    after season 3 ht = 2^2-1-1
    after season 4 ht = 2^3-1
    after season 5 ht = 2^4-1-1
    after season 6 ht = 2^4-1 and so on
    Hence this forms two AP's:
    one : 0, 2, 4, 6, 8, 10, 12,.... (corresponding to the even seasons)
    and : 1, 2, 3, 4, 5, 6, 7, .....  (corresponding to exponent of 2 in even seasons
    since we know the season, we have to find the corresponding term in 2nd AP
    """
    if seasons%2 != 0:
        seasons += 1
        ht_appendage = -1
    else:
        ht_appendage = 0
    n = int(seasons/2) + 1 #this is exponent of 2 needed
    ht_season = int(pow(2, n)) - 1 + ht_appendage
    return ht_season


def main():
    test_cases = int(input().strip())
    for i in range(test_cases):
        print(find_growth(int(input().strip())))
    
if __name__ == '__main__':
    main()