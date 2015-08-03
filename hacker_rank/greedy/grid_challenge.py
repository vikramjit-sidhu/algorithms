"""
Hacker Rank - Grid Challenge
https://www.hackerrank.com/challenges/grid-challenge
"""

def sort_char_list(char_list):
    """ Sort a char list in lexicographic order """
    return sorted(char_list)
    
def check_row_lexicographic_order(char_grid, row_num):
    """ Given a grid of chars, checks if it is in lexicographic order """
    curr_char = char_grid[row_num][0]
    for char in char_grid[row_num][1:]:
        if curr_char > char:
            return False
        current_char = char
    return True

def check_col_lexicographic_order(char_grid, col_num):
    """ In char_grid, checks lexicographic ordering of a column """
    # the first char in col_num, using it as a base of comparision
    curr_char = char_grid[0][col_num]
    row_num = 1
    while row_num < len(char_grid):
        if curr_char > char_grid[row_num][col_num]:
            return False
        curr_char = char_grid[row_num][col_num]
        row_num += 1
    return True

def check_lexicographic_sort(num_elts, char_grid):
    """
    Check lexicographic ordering of a char grid, both row and column wise
    First the rows need to be sorted in lexicographic order before check is done
    """
    # sorting each row of char grid, which is stored as a char list
    for i in range(num_elts):
        char_grid[i] = sort_char_list(char_grid[i])
    #checking rows and cols are in lexicographic order
    for i in range(num_elts):
        # No need to check lexicographic ordering of row as it is already sorted
        # if (not check_row_lexicographic_order(char_grid, i)):
            # return False
        if not check_col_lexicographic_order(char_grid, i):
            return False
    return True

def main():
    num_cases = int(input().strip())
    # Taking the input from stdin
    for i in range(num_cases):
        num_elts = int(input().strip())
        char_grid = []
        # building grid of characters
        for i in range(num_elts):
            # the input is in form of a string, it has to be split into its characters
            char = input().strip()
            char_grid.append([char[i] for i in range(len(char))])
        if (check_lexicographic_sort(num_elts, char_grid)):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()
