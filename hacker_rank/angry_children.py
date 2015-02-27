"""
Hacker Rank Angry Children
https://www.hackerrank.com/challenges/angry-children
Select K integers from the list such that its unfairness is minimized
unfairness = max(x1, x2, ... xk) - min(x1, x2, ... xk)
"""

def min_unfairness(num_list, k):
    nums_sorted = sorted(num_list)
    if k <= 1:
        return nums_sorted[0]
    # assert(k>1) #this is precondition for loop
    min_unfairness = float('inf')   #min unfairness seen so far
    unf_list = []    #list of unfairness, keeps track of the 'k' unfairness integers seen so far.
    prev_elt = 0
    k_counter = 0   #keeps track of how many elements are in set
    for num in nums_sorted:
        k_counter += 1
        if k_counter > k:
            k_counter -= 1
            if min_unfairness > unf_list[0]:
                min_unfairness = unf_list[0]
            del(unf_list[0])
        elif k == 1:
            prev_elt = num
            continue
        delta = prev_elt - num
        unf_list = [i + delta for i in unf_list]
        unf_list.append(delta)
        prev_elt = num
    return min_unfairness
        
def main():
    n = int(input().strip())
    k = int(input().strip())
    num_list = []
    for i in range(n):
        num_list.append(int(input().strip()))
    print(min_unfairness(num_list, k))
        
if __name__ == '__main__':
	main()