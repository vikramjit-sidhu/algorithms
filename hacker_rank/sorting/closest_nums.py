"""
Closest numbers
https://www.hackerrank.com/challenges/closest-numbers
"""

def find_min_diff(num_list):
    sort_num_list = sorted(num_list)
    diff_list = []
    for i in range(len(num_list)-1):
        diff_list.append(sort_num_list[i+1] - sort_num_list[i])
    min_diff = sorted(diff_list)[0]
    for index, elt in enumerate(diff_list):
        if elt == min_diff:
            print('{0} {1}'.format(sort_num_list[index], sort_num_list[index+1]), end=' ')

def main():
    num_elt = int(input().strip())
    num_list = [int(i) for i in input().strip().split(' ')]
    find_min_diff(num_list)
    
if __name__ == '__main__':
    main()