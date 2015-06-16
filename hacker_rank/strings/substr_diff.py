"""
Hacker Rank - Substring diff
https://www.hackerrank.com/challenges/substring-diff
"""

from array import array

def longest_common_substring(str1, str2):
    """
    Finding LCS using dynamic porgramming
    matrix is represented using list of lists
    """
    matrix = []
    for i, char2 in enumerate(str2):
        #i is row index
        row = array('I')
        for j, char1 in enumerate(str1):
            #j is column index
            if char1 == char2:
                if i > 0 and j > 0:
                    row.append(matrix[i-1][j-1] + 1)
                else:
                    row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix
    
def optimise_mismatches(sub_word, start, stop, num_mismatches, s):
    """
    Given a list a non-match is represented by 0, a match by any other number, the first match is given by 1, the second consecutive
    match is then 2, and so on.
    Find the max.
    start and stop are indices
    num_mismatches is the number of mismatches so far
    s is num mismatches required
    """
    if start == 0 or stop == (len(sub_word)-1) or num_mismatches == s:
        return (stop-start+1)
    if sub_word[start-1] == 0:
        left = optimise_mismatches(sub_word, start-1, stop, num_mismatches+1, s)
    else:
        left = optimise_mismatches(sub_word, start-1, stop, num_mismatches, s)
    if sub_word[stop+1] == 0:
        right = optimise_mismatches(sub_word, start, stop+1, num_mismatches+1, s)
    else:
        right = optimise_mismatches(sub_word, start, stop+1, num_mismatches, s)
    return max(left, right)
    

def find_diff(s, p, q):
    matrix = longest_common_substring(p, q)
    row_limit, col_limit = len(matrix)-1, len(matrix[0])-1
    #finding length of maximum substring
    len_substr = 0
    r_end, c_end = -1, -1   #the row and column indices of the last match in substring
    r, c = -1, -1
    for index, row in enumerate(matrix):
        temp = max(row)
        if temp > len_substr:
            len_substr = temp
            r = index
            c = row.index(len_substr)
    #extracting the diagonal which contains the longest substring into a list
    sub_word = []
    r_end, c_end = r+1, c+1
    #sub_word is the diagonal column created which contains the maximum substring
    while r >= 0 and c >= 0:
        sub_word.insert(0, matrix[r][c])
        r, c = r-1, c-1
    while r_end <= row_limit and c_end <= col_limit:
        sub_word.append(matrix[r_end][c_end])
        r_end, c_end = r_end + 1, c_end + 1
    stop = sub_word.index(len_substr)
    start = stop - len_substr + 1
    len_main = optimise_mismatches(sub_word, start, stop, 0, s)
    return len_main

def main():
    num_cases = int(input().strip())
    for i in range(num_cases):
        s, p, q = input().strip().split(' ')
        s = int(s)
        print(find_diff(s, p, q))

if __name__ == '__main__':
    main()