"""
Hacker Rank - Ice Cream parlour
https://www.hackerrank.com/challenges/icecream-parlor
"""

def find_price(m, size_list, num_list):
    sort_list = sorted(num_list)
    first_index, second_index = -1, -1
    for i in range(1, (m//2)+1):
        if binary_search(sort_list, i):
            second_price = m - i
            if binary_search(sort_list, second_price):
                first_index, second_index = find_indices(num_list, i, second_price)
                break
    return (first_index, second_index)
        
def find_indices(li, first_elt, second_elt):
    """ Returns 1 based indexing (starts from 1) """
    index1, index2 = li.index(first_elt), li.index(second_elt)
    if index1 == index2:
        index2 = index1 + 1 + li[index1+1:].index(second_elt)
    if index1 > index2:
        index1, index2 = index2, index1
    return (index1+1, index2+1)
        
def binary_search(li, elt):
    if len(li) > 0:
        mid = len(li) // 2
        if elt == li[mid]:
            return True
        elif elt < li[mid]:
            return binary_search(li[:mid], elt)
        else:
            return binary_search(li[mid+1:], elt)
    return False

def main():
    num_cases = int(input().strip())
    for i in range(num_cases):
        m = int(input().strip())
        size_list = int(input().strip())
        num_list = [int(i) for i in input().strip().split(' ')]
        first, second = find_price(m, size_list, num_list)
        print(first, second)

if __name__ == '__main__':
    main()