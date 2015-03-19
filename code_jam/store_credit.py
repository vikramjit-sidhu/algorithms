"""
Google code jam question - Practice
https://code.google.com/codejam/contest/351101/dashboard#s=p0
"""
import pdb
def binary_search(list, start, end, item):
    if start > end:
        return False
    mid = start + (end-start)//2
    if (item == list[mid]):
        return True
    elif list[mid] > item:
        return binary_search(list, start, mid-1, item)
    else:
        return binary_search(list, mid+1, end, item)
            
def find_items(store_credit, store_items, num_store_items):
    """ Running time is nlog(n), sorting items first and then using binary search """
    sorted_store_items = sorted(store_items)
    for index, item  in enumerate(store_items):
        item_tofind = store_credit - item
        if binary_search(sorted_store_items, 0, num_store_items-1, item_tofind):
            item_tofind_index = store_items.index(item_tofind)
            if item_tofind_index == index:
                try:
                    item_tofind_index = index + 1 + store_items[index+1:].index(item_tofind)
                except Exception:
                    continue
            return (index, item_tofind_index)
    return (-1, -1) #should not execute

def main():
    num_testcases = int(input().strip())
    for i in range(num_testcases):
        store_credit = int(input().strip())
        num_items = int(input().strip())    #the number of items in store, 2 of these are selected
        store_items = [int(i) for i in input().strip().split(' ')]
        item1, item2 = find_items(store_credit, store_items, num_items)
        print("Case #{0}: {1} {2}".format(i+1, item1+1, item2+1))

if __name__ == '__main__':
    main()