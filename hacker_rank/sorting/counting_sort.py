"""
Counting sort
"""

def counting_sort(ar1):
    return count_freq(ar1)

def count_freq(ar1):
    ar_count = [0] * 100
    for elt in ar1:
        ar_count[elt] += 1
    return ar_count

def print_ar(ar1):
    for index, num in enumerate(ar1):
        for j in range(num):
            print(index, end=' ')
    print()
    
def main():
    num_elt = int(input().strip())
    ar1 = [int(i) for i in input().strip().split(' ')]
    ar1 = counting_sort(ar1)
    print_ar(ar1)

if __name__ == '__main__':
    main()