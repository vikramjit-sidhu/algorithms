"""
Quicksort in place
"""

def quicksort(ar1, low, high):
    if low < high:
        ar1, pivot_index = pivot_partition(ar1, low, high)
        print_ar(ar1)
        ar1 = quicksort(ar1, low, pivot_index-1)
        ar1 = quicksort(ar1, pivot_index+1, high)
    return ar1

def pivot_partition(ar1, low, high):
    pivot = ar1[high]
    swap_index = low
    while low < high:
        if ar1[low] < pivot:
            ar1[low], ar1[swap_index] = ar1[swap_index], ar1[low]
            swap_index += 1
        low += 1
    ar1[swap_index], ar1[high] = ar1[high], ar1[swap_index]
    return (ar1, swap_index)
    
def validate_output(ar1):
    """ Validate that the output is correct """
    for i in range(0, len(ar1) - 2):
        if ar1[i] > ar1[i+1]:
            print("WORMHOLE DETECTED")
            return
    print("successful")
    
def print_ar(ar1):
    for num in ar1:
        print(num, end= ' ')
    print()
    
def main():
    num_elt = int(input().strip())
    ar1 = [int(i) for i in input().strip().split(' ')]
    ar1 = quicksort(ar1, 0, len(ar1)-1)

if __name__ == '__main__':
    main()