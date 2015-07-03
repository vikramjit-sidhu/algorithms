"""
Hacker Rank - Fibonacci modified
https://www.hackerrank.com/challenges/fibonacci-modified
"""


def find_term(first, second, term_find):
    fib_nums = {}
    fib_nums[1], fib_nums[2] = first, second
    for i in range(3, term_find+1):
        fib_nums[i] = fib_nums[i-1]**2 + fib_nums[i-2]
    return fib_nums[term_find]

def main():
    first, second, term_find = (int(i) for i in input().strip().split(' '))
    print(find_term(first, second, term_find))

if __name__ == '__main__':
    main()
