"""
Google code jam question - Practice
https://code.google.com/codejam/contest/351101/dashboard#s=p0
"""

def binary_search(list, item):
    """ Returns True if item found in list """
    mid = len(list) // 2
    if item == list[mid]:
        return True
    elif list[mid] > item:
        

def find_items(store_credit, store_items):
    """ Running time is nlog(n), sorting items first and then using binary search """
    sorted_items = sorted(store_items)


def main():
    num_testcases = int(input().strip())
    for i in range(num_testcases):
        store_credit = int(input().strip())
        num_items = int(input().strip())    #the number of items in store, 2 of these are selected
        store_items = [int(i) for i in input().strip().split(' ')]
        item1, item2 = find_items(store_credit, store_items)
        print("Case #{0}: {1} {2}".format(i+1, item1, item2))

if __name__ == '__main__':
    main()