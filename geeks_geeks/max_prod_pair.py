"""
Geeks for geeks - Find pair with maximum product
http://www.geeksforgeeks.org/return-a-pair-with-maximum-product-in-array-of-integers/
"""

def find_max_pair(num_list):
    max_index = abs_max_in_list(num_list)
    max_elt = num_list[max_index]
    num_list[max_index] = 0
    second_max_index = abs_max_in_list(num_list)
    second_max = num_list[second_max_index]
    return (max_elt, second_max)
    
def abs_max_in_list(num_list):
    max, max_index = num_list[0], 0
    for index, num in enumerate(num_list[1:]):
        if abs(num) > max:
            max, max_index = abs(num), (index+1)
    return max_index

def main():
    num_list = [int(i) for i in input().strip().split(", ")]
    print(find_max_pair(num_list))

if __name__ == '__main__':
    main()