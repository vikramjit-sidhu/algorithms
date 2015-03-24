"""
Hacker Rank - Chocolate Feast
https://www.hackerrank.com/challenges/chocolate-feast

n -> amount that little bob has 
c -> cost of each chocolate
m -> amount of wrappers given to store
"""

def find_chocs(n, c, m):
    num_chocs = (n // c)
    extra_chocs = num_chocs // m    #the chocolates obtained by exchanging wrappers
    rem_chocs = num_chocs % m   #the chocolates whose wrappers are not used for exchange
    while extra_chocs != 0:
        num_chocs += extra_chocs
        extra_chocs, rem_chocs = (extra_chocs + rem_chocs) // m, (extra_chocs + rem_chocs) % m
    return num_chocs

def main():
    test_cases = int(input().strip())
    for i in range(test_cases):
        n, c, m = [int(i) for i in input().strip().split(' ')]
        print(find_chocs(n, c, m))

if __name__ == '__main__':
    main()