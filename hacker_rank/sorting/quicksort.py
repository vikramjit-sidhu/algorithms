"""
Quicksort Algorithm
"""

def quicksort(ar1):
    if len(ar1) > 1:
        pivot, arLow, arHigh = pivot_partition(ar1)
        arLowSort = quicksort(arLow)
        arHighSort = quicksort(arHigh)
        ar1 = arLowSort
        ar1.append(pivot)
        ar1.extend(arHighSort)
        print_ar(ar1)
    return ar1
    
def pivot_partition(ar1):
    """ Pivot is 1st element """
    pivot = ar1[0]
    smaller, greater = [], []
    for num in ar1[1:]:
        if num < pivot:
            smaller.append(num)
        else:
            greater.append(num)
    return (pivot, smaller, greater)
            
def print_ar(ar1):
    for num in ar1:
        print(num, end= ' ')
    print()
    
def main():
    num_elt = int(input().strip())
    ar1 = [int(i) for i in input().strip().split(' ')]
    ar1 = quicksort(ar1)

if __name__ == '__main__':
    main()