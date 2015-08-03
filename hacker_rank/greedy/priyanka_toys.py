"""
Hacker Rank - Priyanka and Toys
https://www.hackerrank.com/challenges/priyanka-and-toys
"""

def sort_list(list_tosort):
    """ Returns a sorted list """
    return sorted(list_tosort)

def calculate_toys_obtained_for_free(weight_list, index, num_toys):
    """
    The toy in list at 'index' position has been bought, 
    find which toys are gotten for free (in range [w, w+4])
    """
    weight_range_high = weight_list[index] + 4
    while (index < num_toys):
        if (weight_list[index] > weight_range_high):
            break
        index += 1
    return index
    
def find_min_units_to_buy_toys(num_toys, toy_weight_list):
    """
    Given that each toy costs 1 unit, on buying a toy of w weight, 
    all toys in range [w, w+4] come free. All toys must be bought
    Iterating through list, and finding which toys to spend units on
    """
    # sorting weight list
    sorted_wt_list = sort_list(toy_weight_list)
    index = 0
    units = 0   # the number of units used
    while (index < num_toys):
        units += 1
        index = calculate_toys_obtained_for_free(sorted_wt_list, index, num_toys)
    return units
    
def main():
    num_toys = int(input().strip())
    toy_weight_list = [int(i) for i in input().strip().split(' ')]
    print(find_min_units_to_buy_toys(num_toys, toy_weight_list))

if __name__ == "__main__":
    main()