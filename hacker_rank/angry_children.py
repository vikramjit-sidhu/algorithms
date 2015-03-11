"""
Hacker Rank Angry Children
https://www.hackerrank.com/challenges/angry-children
Select K integers from the list such that its unfairness is minimized
unfairness = max(x1, x2, ... xk) - min(x1, x2, ... xk)
"""

def min_unfairness(num_list, k):
    nums_sorted = sorted(num_list)
    # assert(k>1) #this is precondition for loop
    unf_list = []    #list of unfairness, keeps track of the 'k' unfairness integers seen so far.
    start_index = 0
    last_index = k-1
    min_unf = float('inf')
    list_len = len(nums_sorted)
    while last_index < list_len:
        diff = nums_sorted[last_index] - nums_sorted[start_index]
        if diff < min_unf:
            min_unf = diff
        start_index += 1
        last_index += 1
    return min_unf
        
def main():
    n = int(input().strip())
    k = int(input().strip())
    num_list = []
    for i in range(n):
        num_list.append(int(input().strip()))
    print(min_unfairness(num_list, k))
        
if __name__ == '__main__':
	main()