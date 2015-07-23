"""
Geeks for Geeks - Find odd appearing element
http://www.geeksforgeeks.org/find-the-element-that-odd-number-of-times-in-olog-n-time/
"""

import pdb

def find_odd_element(num_list):
    return (recurse_conquer(0, len(num_list)-1, num_list))

def recurse_conquer(low, high, num_list):
    # pdb.set_trace()
    if (low <= high):
        mid = (low + high) // 2
        if mid < high and num_list[mid] == num_list[mid+1]:
            left = recurse_conquer(low, mid-1, num_list)
            right = recurse_conquer(mid+2, high, num_list)
        elif mid > low and num_list[mid] == num_list[mid-1]:
            left = recurse_conquer(low, mid-2, num_list)
            right = recurse_conquer(mid+1, high, num_list)
        else:
            return num_list[mid]
        if left is not None:
            return left
        else:
            return right
    return None
    
def main():
    num_list = [int(i) for i in input().strip().split(", ")]
    odd_elt = find_odd_element(num_list)
    print(odd_elt)

if __name__ == '__main__':
    main()