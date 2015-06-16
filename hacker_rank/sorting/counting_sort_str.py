"""
Counting sort new
"""

def counting_sort(num_list, word_list):
    ar_count = [0] * 100
    for num in num_list:
        ar_count[num] += 1
    return ar_count

def print_ar(ar1):
    sum = 0
    for num in ar1:
        sum += num
        print(sum, end=' ')
    print()

def main():
    num_elt = int(input().strip())
    num_list = []
    word_list = []
    for i in range(num_elt):
        num, word = input().strip().split(' ')
        num_list.append(int(num))
        word_list.append(word)
    ar1 = counting_sort(num_list, word_list)
    print_ar(ar1)

if __name__ == '__main__':
    main()