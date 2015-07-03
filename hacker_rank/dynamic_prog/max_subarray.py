"""
Hacker Rank - The Maximum Subarray
https://www.hackerrank.com/challenges/maxsubarray
"""

memo_conti = None
memo_nconti = None

def find_subarrays(list_size, num_list):
    """
    Finding largest contiguous and non-contiguous sub-arrays of num_list
    At least one element should be in each sub-array
    """
    global memo_conti, memo_nconti
    memo_conti = [[None]*list_size for i in range(list_size)]
    conti = max_contiguous_subarray(0, list_size-1, num_list)
    del memo_conti
    memo_nconti = [[None]*list_size for i in range(list_size)]
    non_conti = max_non_contiguous_subarray(0, list_size-1, num_list)
    del memo_nconti
    return conti, non_conti

def max_contiguous_subarray(start, stop, num_list):
    global memo_conti
    if start == stop:
        memo_conti[start][start] = num_list[start]
        return num_list[start]
    if memo_conti[start][stop] is not None:
        return memo_conti[start][stop]
    memo_conti[start][stop] = max(num_list[start] + max_contiguous_subarray(start+1, stop, num_list), + \
                              num_list[stop] + max_contiguous_subarray(start, stop-1, num_list))
    return memo_conti[start][stop]
    
def max_non_contiguous_subarray(start, stop, num_list):
    global memo_nconti
    if start == stop:
        memo_nconti[start][start] = num_list[start]
        return num_list[start]
    if memo_nconti[start][stop] is not None:
        return memo_nconti[start][stop]
    memo_nconti[start][stop] = max(num_list[start] + max_non_contiguous_subarray(start+1, stop, num_list), + \
                              num_list[stop] + max_non_contiguous_subarray(start, stop-1, num_list), + \
                              max_non_contiguous_subarray(start+1, stop, num_list), + \
                              max_non_contiguous_subarray(start, stop-1, num_list))
    return memo_nconti[start][stop]

def main():
    num_cases = int(input().strip())
    for i in range(num_cases):
        list_size = int(input().strip())
        num_list = [int(i) for i in input().strip().split(' ')]
        contiguous, non_contiguous = find_subarrays(list_size, num_list)
        print('{0} {1}'.format(contiguous, non_contiguous))

if __name__ == '__main__':
    main()