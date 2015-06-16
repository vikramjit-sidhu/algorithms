"""
Sherlock and Arrays
https://www.hackerrank.com/challenges/sherlock-and-array
"""

def find_sentinel(size_list, num_list):
    sum_list = sum(num_list)
    sum_first, sum_second = 0, sum_list
    for i in range(size_list):
        curr_elt = num_list[i]
        sum_second -= curr_elt
        if sum_second == sum_first:
            print('YES')
            return
        sum_first += curr_elt
    print('NO')

def main():
    num_cases = int(input().strip())
    for i in range(num_cases):
        size_list = int(input().strip())
        num_list = [int(i) for i in input().strip().split(' ')]
        find_sentinel(size_list, num_list)

if __name__ == '__main__':
    main()