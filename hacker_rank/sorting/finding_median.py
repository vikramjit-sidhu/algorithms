"""
Finding the median
https://www.hackerrank.com/challenges/find-median
"""

def find_median(num_list, low, high, mid):
    if low < high:
        num_list, partition_index = partition_list(num_list, low, high)
        if partition_index == mid:
            return num_list
        num_list = find_median(num_list, low, partition_index-1, mid)
        num_list = find_median(num_list, partition_index+1, high, mid)
    return num_list
    
def partition_list(num_list, low, high):
    pivot = num_list[high]
    swap_index = low
    while low < high:
        if num_list[low] < pivot:
            num_list[swap_index], num_list[low] = num_list[low], num_list[swap_index]
            swap_index += 1
        low += 1
    num_list[high], num_list[swap_index] = num_list[swap_index], num_list[high]
    return (num_list, swap_index)

def main():
    num_elt = int(input().strip())
    num_list = [int(i) for i in input().strip().split(' ')]
    mid = len(num_list) // 2
    num_list = find_median(num_list, 0, num_elt-1, mid)
    print(num_list[mid])
    
if __name__ == '__main__':
    main()