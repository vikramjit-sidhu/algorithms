"""
Sherlock and watson
https://www.hackerrank.com/challenges/sherlock-and-watson
"""

def print_circular_idx(num_list, idx_list, num_rotations):
    len_list = len(num_list)
    rot_list = [0] * len_list
    for index, elt in enumerate(num_list):
        rot_list[(index+num_rotations) % len_list] = elt
    for idx in idx_list:
        print(rot_list[idx])

def main():
    n, k, q = (int(i) for i in input().strip().split())
    num_list = [int(i) for i in input().strip().split()]
    idx_list = []
    for i in range(q):
        idx_list.append(int(input().strip()))
    print_circular_idx(num_list, idx_list, k)

if __name__ == '__main__':
    main()