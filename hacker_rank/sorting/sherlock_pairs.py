"""
Sherlock and pairs
https://www.hackerrank.com/challenges/sherlock-and-pairs
"""

def match_pairs(len_ar, num_list):
    count_pairs = 0
    sort_list = sorted(num_list)
    #count num of elements which are the same and find the permutation of them
    #eg 1 1 1 -> 3 1's P(3, 2)
    same_elts = 1
    for i in range(len_ar-1):
        if sort_list[i] == sort_list[i+1]:
            same_elts += 1
        else:
            count_pairs += same_elts * (same_elts-1)
            same_elts = 1
    count_pairs += same_elts * (same_elts-1)
    print(count_pairs)

def main():
    test_cases = int(input().strip())
    for i in range(test_cases):
        len_ar = int(input().strip())
        num_list = [int(i) for i in input().strip().split(' ')]
        match_pairs(len_ar, num_list)

if __name__ == '__main__':
    main()