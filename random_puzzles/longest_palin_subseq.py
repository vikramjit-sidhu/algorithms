"""
Longest palindrome subsequence
"""

memo = None
ps = ''

def lps(sequence):
    global memo
    memo = [[None]*len(sequence) for i in range(len(sequence))]
    return find_subproblems(sequence, 0, len(sequence)-1)
    
def find_subproblems(sequence, low, high):
    global memo, ps
    if memo[low][high] is not None:
        return memo[low][high]
    if low == high:
        memo[low][high] = 1 #base case, if characters are the same, then 1 can be added to palin length
    elif low < high:
        if sequence[low] == sequence[high]:
            memo[low][high] = 2 + find_subproblems(sequence, low+1, high-1)
        else:
            memo[low][high] = max(find_subproblems(sequence, low, high-1), find_subproblems(sequence, low+1, high))
    return memo[low][high]

def main():
    sequence = input().strip()  #word to find palindromic subsequence in
    print(lps(sequence))
    for line in memo:
        print(line)
    
if __name__ == '__main__':
    main()