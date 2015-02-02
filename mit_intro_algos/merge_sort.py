"""
Merge sort algorithm in python
"""
import random


def merge(ar1, ar2):
    """
    Given two arrays, merge them in sorted order.
    Infinity float("inf") is appended to end of each array, so that end of array check does not need to be done
    """
    ar_all = (len(ar1)+len(ar2))*[int]
    infinity = float("inf")
    ar1.append(infinity)
    ar2.append(infinity)
    index1, index2 = 0, 0
    
    for i in range(0, len(ar_all)):
        if ar1[index1] < ar2[index2]:
            ar_all[i] = ar1[index1]
            index1+=1
        else:
            ar_all[i] = ar2[index2]
            index2 += 1
    return ar_all
    

def merge_sort(ar):
    """
    Find mid point of array, and splicing it into 2 sub-arrays, ar_lower, ar_higher
    ar_lower = ar[0-mid]
    ar_higher = ar[mid+1 - end]
    when ar_lower and ar_higher return, they are sorted and need to be merged to form a larger array
    """
    mid = int(len(ar)/2)
    if mid > 0:
        ar_lower = merge_sort(ar[:mid])
        ar_higher = merge_sort(ar[mid:])
        ar = merge(ar_lower, ar_higher)
    return ar    

    
def check_list_sorted(ar1):
    """
    checks if an array/list is sorted
    """
    return all(ar1[i] >= ar1[i-1] for i in range(1, len(ar1)))
    
    
def main():
    array_size = 1000000 #1 mil
    numbers_range = 10000000 #10 mil
    foo_ar = random.sample(range(0, numbers_range), array_size)
    
    print("before merge_sort, is list sorted: {0}".format(check_list_sorted(foo_ar)))
    foo_ar = merge_sort(foo_ar)
    print("after merge_sort, is list sorted: {0}".format(check_list_sorted(foo_ar)))


if __name__ == '__main__':
    main()