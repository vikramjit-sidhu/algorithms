"""
Hacker Rank - Service Lane
https://www.hackerrank.com/challenges/service-lane
"""

def main():
    len_freeway, num_cases = (int(i) for i in input().strip().split(' '))
    width_list = [int(i) for i in input().strip().split(' ')]
    for i in range(num_cases):
        i, j = (int(l) for l in input().strip().split(' '))
        min_width = float('inf')
        for index in range(i, j+1):
            if width_list[index] < min_width:
                min_width = width_list[index]
        if min_width >= 3:
            print('3')
        elif min_width >= 2:
            print('2')
        elif min_width >= 1:
            print('1')

if __name__ == '__main__':
	main()