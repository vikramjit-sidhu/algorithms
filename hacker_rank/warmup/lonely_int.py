"""
Hacker rank challenge
N integers in array, all but one integer occur in pairs
https://www.hackerrank.com/challenges/lonely-integer
"""

def find_bachelor(nums):
    xord = 0
    for num in nums:
        xord = xord ^ num
    return xord

def main():
    n = int(input())
    nums = [int(i) for i in input().strip().split()]
    print(find_bachelor(nums))

if __name__ == '__main__':
    main()