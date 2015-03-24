"""
Hacker Rank - Haloween Party
https://www.hackerrank.com/challenges/halloween-party
"""

def find_choc_pieces(num_cuts):
    """
    given an infinite sq, find no of 1X1 pieces possible with
    num_cuts totally
    """
    horiz_cuts = num_cuts // 2
    ver_cuts = num_cuts - horiz_cuts
    return horiz_cuts*ver_cuts

def main():
    num_cases = int(input().strip())
    for i in range(num_cases):
        num_cuts = int(input().strip())
        print(find_choc_pieces(num_cuts))

if __name__ == '__main__':
    main()