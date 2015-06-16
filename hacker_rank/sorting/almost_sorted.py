"""
Almost Sorted
https://www.hackerrank.com/challenges/almost-sorted
"""

import pdb

def find_operation(num_list, len_list):
    rev, swap = False, False
    rev_start, rev_stop = -1, -1
    swap_first, swap_second = -1, -1
    idx = 0
    len_list -= 1   #iterating till the second to last index
    # pdb.set_trace()
    while idx < len_list:
        if num_list[idx] > num_list[idx+1]:
            if swap:
                print('no')
                return
            elif rev:
                #checking if swap is possible
                if (rev_stop - rev_start) == 1:
                    rev, swap = False, True
                    #for swap a peak is needed, which is at rev_start
                    swap_first = rev_start
                    #now finding a valley (peak and valley are mathematically speaking)
                    while idx < len_list:
                        if (num_list[idx] < num_list[idx-1]) and (num_list[idx] < num_list[idx+1]):
                            swap_second = idx
                            break
                        idx += 1
                #swap not possible, list cannot be sorted with just one op
                else:
                    print('no')
                    return
            else:
                rev = True
                rev_start = idx
                while idx < len_list and num_list[idx] > num_list[idx+1]:
                    idx += 1
                rev_stop = idx
        idx += 1
    #checking if reverse is actually a swap
    if rev and ((rev_stop-rev_start) == 1):
        rev, swap = False, True
        swap_first, swap_second = rev_start, rev_stop
    if rev:
        #checking boundary conditions, after reversing, the elements should be in increasing order, so just checking boundaries
        if rev_start > 0:
            if num_list[rev_stop] < num_list[rev_start-1]:
                print('no')
                return
        if rev_stop < len_list:
            if num_list[rev_start] > num_list[rev_stop+1]:
                print('no')
                return
        print('yes')
        print('reverse {0} {1}'.format(rev_start+1, rev_stop+1))
    elif swap:
        #checking if array will be sorted after swapping
        if swap_first > 0:
            if num_list[swap_second] < num_list[swap_first-1]:
                print('no')
                return
        if num_list[swap_second] > num_list[swap_first+1]:
            print('no')
            return
        if swap_second < len_list:
            if num_list[swap_first] > num_list[swap_second+1]:
                print('no')
                return
        if num_list[swap_first] < num_list[swap_second-1]:
            print('no')
            return
        print('yes')
        print('swap {0} {1}'.format(swap_first+1, swap_second+1))
    else:
        print('no')
    
def main():
    n = int(input().strip())
    num_list = [int(i) for i in input().strip().split(' ')]
    find_operation(num_list, n)
    
if __name__ == '__main__':
    main()