"""
Hacker Rank - Cut the sticks
https://www.hackerrank.com/challenges/cut-the-sticks
"""

def find_num_cuts(num_elts, num_list):
    # sort the list
    num_list = sort_list(num_list)
    # keep track of the current smallest element in array
    smallest_elt_index = 0
    # the last index in the list is used as an exit condition
    while (smallest_elt_index < num_elts):
        # get new list, with smallest elt subtracted from each elt and num of elements that this happens to
        num_list, num_elts_subtracted_from = subtract_smallest_elt(num_list, smallest_elt_index)
        # find new smallest element
        smallest_elt_index = find_new_smallest_elt_index(num_list, smallest_elt_index)
        print(num_elts_subtracted_from)

def sort_list(num_list):
    return sorted(num_list)

def subtract_smallest_elt(num_list, smallest_elt_index):
    """
    Subtract the element at smallest_elt_index from each of the elements after it,
    return new list and the number of elements which are subtracted
    """
    num_elts_sub = 0
    curr_index = smallest_elt_index
    smallest_elt = num_list[smallest_elt_index]
    while (curr_index < len(num_list)):
        num_list[curr_index] -= smallest_elt
        num_elts_sub += 1
        curr_index += 1
    return (num_list, num_elts_sub)
    
def find_new_smallest_elt_index(num_list, smallest_elt_index):
    """ Finds new smallest element index and returns it """
    while ((smallest_elt_index < len(num_list)) and (num_list[smallest_elt_index] == 0)):
        smallest_elt_index += 1
    return smallest_elt_index
        
def main():
    num_elts = int(input().strip())
    num_list = [int(i) for i in input().strip().split(' ')]
    find_num_cuts(num_elts, num_list)

if __name__ == '__main__':
    main()
    