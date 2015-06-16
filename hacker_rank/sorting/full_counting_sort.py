"""
Full counting sort
https://www.hackerrank.com/challenges/countingsort4
"""

def countin_sort(num_list, word_list):
    sorted_nums = [0] * 100
    first_half = {}
    second_half = {}
    mid = len(num_list) // 2
    for i in range(mid):
        sorted_nums[num_list[i]] += 1
        if num_list[i] in first_half:
            first_half[num_list[i]].append(word_list[i])
        else:
            first_half[num_list[i]] = [word_list[i]]
    for i in range(mid, len(num_list)):
        sorted_nums[num_list[i]] += 1
        if num_list[i] in second_half:
            second_half[num_list[i]].append(word_list[i])
        else:
            second_half[num_list[i]] = [word_list[i]]
    print_ars(first_half, second_half, sorted_nums)

def print_ars(first_half, second_half, sorted_nums):
    for index, val in enumerate(sorted_nums):
        if val == 0:
            continue
        if index in first_half:
            for item in first_half[index]:
                print('-', end=' ')
        if index in second_half:
            for item in second_half[index]:
                print(item, end=' ')

def main():
    num_elt = int(input().strip())
    num_list, word_list = [], []
    for i in range(num_elt):
        num, word = input().strip().split(' ')
        num_list.append(int(num))
        word_list.append(word)
    countin_sort(num_list, word_list)
    
if __name__ == '__main__':
    main()