"""
Insertion sort analysis
https://www.hackerrank.com/challenges/insertion-sort
"""

def find_shifts(num_list, list_size):
    """
    Using merge sort technique
    Same as merge sort, count shifts during merge process
    This is found during the merging of two lists, finding num of shifts for the latter list.
    """
    sort_list, num_shifts = merge_sort(num_list, list_size, 0)
    return num_shifts

def merge_sort(num_list, list_size, num_shifts):
    if list_size > 1:
        mid = list_size // 2
        #sorting the left list, and findng num of shifts
        list_left = num_list[:mid]
        list_left, num_shifts = merge_sort(list_left, len(list_left), num_shifts)
        #sorting the right list, and findng num of shifts
        list_right = num_list[mid:]
        list_right, num_shifts = merge_sort(list_right, len(list_right), num_shifts)
        num_list, new_shifts = merge(list_left, list_right)
        #adding new shifts to num of shifts already present and returning values
        num_shifts += new_shifts
    return (num_list, num_shifts)
    
def merge(left_list, right_list):
    left_idx, right_idx = 0, 0
    left_len, right_len = len(left_list), len(right_list)
    sort_list = []
    num_shifts = 0
    while left_idx < left_len and right_idx < right_len:
        if left_list[left_idx] <= right_list[right_idx]:
            sort_list.append(left_list[left_idx])
            left_idx += 1
        else:
            num_shifts += left_len - left_idx
            sort_list.append(right_list[right_idx])
            right_idx += 1
    if left_idx < left_len:
        sort_list.extend(left_list[left_idx:])
    elif right_idx < right_len:
        sort_list.extend(right_list[right_idx:])
    return (sort_list, num_shifts)
    
def main():
    test_cases = int(input().strip())
    for i in range(test_cases):
        list_size = int(input().strip())
        num_list = [int(i) for i in input().strip().split(' ')]
        print(find_shifts(num_list, list_size))

if __name__ == '__main__':
    main()