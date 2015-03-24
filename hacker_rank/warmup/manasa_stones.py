"""
Hacker Rank - Manasa and Stones
https://www.hackerrank.com/challenges/manasa-and-stones
"""

def last_stone_values(n, a, b):
    old_set = {0}
    new_set = set()
    for i in range(n-1):
        for poss_val in old_set:
            new_set.add(poss_val+a)
            new_set.add(poss_val+b)
        old_set = new_set
        new_set = set()
    return old_set
    
def main():
    num_cases = int(input().strip())
    for i in range(num_cases):
        n = int(input().strip())    #num of stones
        a = int(input().strip())
        b = int(input().strip())
        lsv = last_stone_values(n, a, b)
        for num in sorted(lsv):
            print(num, end=' ')
        print()

if __name__ == '__main__':
    main()