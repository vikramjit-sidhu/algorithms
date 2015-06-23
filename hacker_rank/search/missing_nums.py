"""
Hacker Rank - Missing numbers
https://www.hackerrank.com/challenges/missing-numbers
"""

def find_missing(size_smaller, smaller_list, size_larger, larger_list):
    count_freq_smaller = {} #count the freq of smaller list
    count_freq_larger = {}  #count freq of larger list
    for num in smaller_list:
        if num in count_freq_smaller:
            count_freq_smaller[num] += 1
        else:
            count_freq_smaller[num] = 1
    for num in larger_list:
        if num in count_freq_larger:
            count_freq_larger[num] += 1
        else:
            count_freq_larger[num] = 1
    missing_nums = []
    for key in sorted(count_freq_larger.keys()):
        if (key not in count_freq_smaller) or (count_freq_larger[key] > count_freq_smaller[key]):
            missing_nums.append(key)
    return missing_nums
    

def main():
    size_list1 = int(input().strip())
    num_list1 = [int(i) for i in input().strip().split(' ')]
    size_list2 = int(input().strip())
    num_list2 = [int(i) for i in input().strip().split(' ')]
    missing_nos = find_missing(size_list1, num_list1, size_list2, num_list2)
    for miss in missing_nos:
        print(miss, end=' ')
    

if __name__ == '__main__':
    main()