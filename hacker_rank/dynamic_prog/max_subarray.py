"""
Hacker Rank - The Maximum Subarray
https://www.hackerrank.com/challenges/maxsubarray
"""

memo_nconti = {}

def find_subarrays(list_size, num_list):
    """
    Finding largest contiguous and non-contiguous sub-arrays of num_list
    At least one element should be in each sub-array
    """
    conti = max_contiguous_subarray(num_list, list_size)
    non_conti = max_non_contiguous_subarray_boring(num_list, list_size)
    return conti, non_conti

def max_contiguous_subarray(num_list, list_size):
    """
    Using another array, which will contain the max subarray upto that element of the actual list
    """
    subarray_list = [None] * list_size
    subarray_list[0] = num_list[0]
    sub_index = 0   #current subarray index being considered
    for num in num_list[1:]:
        if num > (subarray_list[sub_index]+num): 
            subarray_list[sub_index+1] = num
        else:
            subarray_list[sub_index+1] = subarray_list[sub_index] + num
        sub_index += 1
    return max(subarray_list)   #the max element in list is the one which is the max subarray sum

def max_non_contiguous_subarray_boring(num_list, list_size):
    subseq_list = [None] * list_size
    subseq_list[0] = num_list[0]
    sub_index = 0
    for num in num_list[1:]:
        if num > (subseq_list[sub_index]+num):
            subseq_list[sub_index+1] = num
        elif (num + subseq_list[sub_index]) < subseq_list[sub_index]:
            subseq_list[sub_index+1] = subseq_list[sub_index]
        else:
            subseq_list[sub_index+1] = subseq_list[sub_index] + num
        sub_index += 1
    return max(subseq_list)
            
def max_non_contiguous_subarray(start, stop, num_list):
    global memo_nconti
    if start == stop:
        memo_nconti[(start, start)] = num_list[start]
        return num_list[start]
    if (start, stop) in memo_nconti:
        return memo_nconti[(start, stop)]
    memo_nconti[(start, stop)] = max(num_list[start] + max_non_contiguous_subarray(start+1, stop, num_list), + \
                                num_list[stop] + max_non_contiguous_subarray(start, stop-1, num_list), + \
                                max_non_contiguous_subarray(start+1, stop, num_list), + \
                                max_non_contiguous_subarray(start, stop-1, num_list))
    return memo_nconti[(start, stop)]

def main():
    num_cases = int(input().strip())
    for i in range(num_cases):
        list_size = int(input().strip())
        num_list = [int(i) for i in input().strip().split(' ')]
        contiguous, non_contiguous = find_subarrays(list_size, num_list)
        print('{0} {1}'.format(contiguous, non_contiguous))

if __name__ == '__main__':
    main()